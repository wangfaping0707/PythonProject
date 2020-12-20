"""
Module providing JSON serialization and de-serialization just like the `json`
module, but with support for more data types (e.g., NumPy arrays).
"""

import base64
import fractions
import io
import json
import warnings

# NumPy is optional (used in the extended JSON encoder/decoder)
try:
    import numpy as np
    _NUMPY_ERROR = None
except ImportError as e:
    _NUMPY_ERROR = e


###
#%% internal helpers
###


class _ExtendedJsonEncoder(json.JSONEncoder):
    """
    JSON encoder which also supports objects of the following types:
    `bytes`, `numpy.ndarray`.

    For decoding, use `ExtendedJsonDecoder.object_hook` as value for the
    `object_hook` parameter of `json.load` or `json.loads`.
    """

    def default(self, o):
        # byte arrays
        if isinstance(o, bytes):
            e = base64.b64encode(o).decode("ascii")
            return {"__ExtendedJsonType__": "bytes", "__ExtendedJsonValue__": e, "__ExtendedJsonEncoding__": "base64"}

        # fractions
        if isinstance(o, fractions.Fraction):
            e = [o.numerator, o.denominator]
            return {"__ExtendedJsonType__": "fractions.Fraction", "__ExtendedJsonValue__": e, "__ExtendedJsonEncoding__": "plain"}

        # NumPy arrays
        if (_NUMPY_ERROR is None) and isinstance(o, np.ndarray):
            b = io.BytesIO()
            np.save(file=b, arr=o, allow_pickle=False, fix_imports=False)
            e = base64.b64encode(b.getvalue()).decode("ascii")
            return {"__ExtendedJsonType__": "numpy.ndarray", "__ExtendedJsonValue__": e, "__ExtendedJsonEncoding__": "base64"}

        # no extended object
        return super().default(o)


class _ExtendedJsonDecoder():
    """
    This class is the counterpart of `ExtendedJsonEncoder` and provides the
    static method `object_hook`.
    """

    @staticmethod
    def object_hook(o):
        # only handle dicts which have the three keys "__ExtendedJsonType__", "__ExtendedJsonValue__", and "__ExtendedJsonEncoding__"
        keys = o.keys()
        if (len(keys) == 3) and ("__ExtendedJsonType__" in keys) and ("__ExtendedJsonValue__" in keys) and ("__ExtendedJsonEncoding__" in keys):
            # byte arrays
            if (o["__ExtendedJsonType__"] == "bytes") and (o["__ExtendedJsonEncoding__"] == "base64"):
                e = o["__ExtendedJsonValue__"]
                b = base64.b64decode(bytes(e, "ascii"))
                return b

            # fractions
            if (o["__ExtendedJsonType__"] == "fractions.Fraction") and (o["__ExtendedJsonEncoding__"] == "plain"):
                (n, d) = o["__ExtendedJsonValue__"]
                f = fractions.Fraction(numerator=n, denominator=d)
                return f

            # NumPy arrays
            if o["__ExtendedJsonType__"] == "numpy.ndarray":
                if _NUMPY_ERROR is None:
                    e = o["__ExtendedJsonValue__"]
                    b = base64.b64decode(bytes(e, "ascii"))
                    x = np.load(file=io.BytesIO(b), allow_pickle=False, fix_imports=False)
                    return x
                else:
                    warnings.warn("Could not decode object of type 'numpy.ndarray', because NumPy import failed: '{}'".format(_NUMPY_ERROR))

        # no extended object
        return o


###
#%% JSON equivalents
###


def dump(*args, **kwargs):
    """
    See :func:`json.dump()`.
    """
    return json.dump(*args, **kwargs)


def dumps(*args, **kwargs):
    """
    See :func:`json.dumps()`.
    """
    kwargs["ensure_ascii"] = True
    kwargs["cls"] = _ExtendedJsonEncoder
    return json.dumps(*args, **kwargs)


def load(*args, **kwargs):
    """
    See :func:`json.load()`.
    """
    kwargs["object_hook"] = _ExtendedJsonDecoder.object_hook
    return json.load(*args, **kwargs)


def loads(*args, **kwargs):
    """
    See :func:`json.loads()`.
    """
    kwargs["object_hook"] = _ExtendedJsonDecoder.object_hook
    return json.loads(*args, **kwargs)
