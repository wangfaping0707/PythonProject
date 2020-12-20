"""
General utility functions.

Written in pure Python, using only modules from the standard library and
third-party modules included in this package to ensure maximum compatibility.
"""

import base64
import collections
import colorsys
import configparser
import copy
import datetime
import errno
import functools
import hashlib
import importlib
import inspect
import itertools
import json
import math
import os
import pprint
import re
import shutil
import time
import warnings

import dh.thirdparty.atomicwrites
import dh.thirdparty.humanize
import dh.thirdparty.tabulate
import dh.thirdparty.tqdm
import dh.thirdparty.transitions


###
#%% iterable-related
###


def cycle(x, length):
    """
    Cycles through the values of `x` until `length` items were yielded.

    >>> list(cycle([1, 2, 3], 5))
    [1, 2, 3, 1, 2]

    .. seealso:: :func:`itertools.cycle` and :func:`itertools.repeat` (they
                 are similar but different).

    .. todo:: handle non-list arguments more efficiently (avoid list() for
              entire `x`)
    """

    # if items can't be accessed by index, create list from x
    if hasattr(x, "__getitem__") and hasattr(x, "__len__"):
        xList = x
    else:
        xList = list(x)

    # cycle loop
    M = len(xList)
    N = length
    for n in range(N):
        yield xList[n % M]


def eqvalue(x):
    """
    Checks whether all values of the iterable `x` are identical and returns
    that value if true, and otherwise raises a `ValueError` exception.

    >>> eqvalue([1, 1, 1])
    1
    """

    items = iter(x)
    first = next(items)
    for item in items:
        if item != first:
            raise ValueError("Values are not identical: {}, {}".format(first, item))
    return first


def flatten(*args):
    """
    Recursively flattens the items of `*args` into one iterable.

    >>> list(flatten(1, [2, 3, [4]]))
    [1, 2, 3, 4]

    >>> list(flatten([[1, []], ('two', [[3.0]]), (None,)]))
    [1, 'two', 3.0, None]
    """

    for arg in args:
        try:
            if isinstance(arg, str):
                raise TypeError()

            # arg is iterable (and not a string)
            for item in arg:
                for item2 in flatten(item):
                    yield item2
        except TypeError:
            # x is not iterable (or a string)
            yield arg


def hzip(x):
    """
    Zips the first and second half of `x`.

    If `x` has odd length, the last element will be ignored.

    >>> list(hzip([1, 2, 3, 4, 5, 6]))
    [(1, 4), (2, 5), (3, 6)]

    >>> list(hzip([1, 2, 3, 4, 5, 6, 7]))
    [(1, 4), (2, 5), (3, 6)]
    """

    N = int(len(x) // 2)
    return zip(x[:N], x[N:])


def minmax(x):
    """
    Returns a tuple containing the min and max value of the iterable `x`.

    .. note:: this also works if `x` is a generator.

    >>> minmax([1, -2, 3, 4, 1, 0, -2, 5, 1, 0])
    (-2, 5)
    """

    (minItem, maxItem) = (None, None)
    for item in x:
        if (minItem is None) or (item < minItem):
            minItem = item
        if (maxItem is None) or (item > maxItem):
            maxItem = item
    return (minItem, maxItem)


def argmin(x):
    """
    Returns the index of the smallest element of the iterable `x`.

    If two or more elements equal the minimum value, the index of the first
    such element is returned.

    >>> argmin([1, 3, 2, 0])
    3

    >>> argmin(abs(x) for x in range(-3, 4))
    3
    """
    argmin_ = None
    min_ = None
    for (nItem, item) in enumerate(x):
        if (argmin_ is None) or (item < min_):
            argmin_ = nItem
            min_ = item
    return argmin_


def argmax(x):
    """
    Returns the index of the largest element of the iterable `x`.

    If two or more elements equal the maximum value, the index of the first
    such element is returned.

    >>> argmax([1, 3, 2, 0])
    1

    >>> argmax(-abs(x) for x in range(-3, 4))
    3
    """
    argmax_ = None
    max_ = None
    for (nItem, item) in enumerate(x):
        if (argmax_ is None) or (item > max_):
            argmax_ = nItem
            max_ = item
    return argmax_


def unique(x):
    """
    Yields unique values of `x`, preserving the order of the items.

    >>> list(unique((1, 2, 1, 3)))
    [1, 2, 3]

    >>> list(unique((1, 1.0, '1', 'one')))
    [1, '1', 'one']

    .. seealso:: :func:`numpy.unique` for NumPy arrays.
    """

    seen = []
    for item in x:
        if item not in seen:
            yield item
            seen.append(item)


def uids(x):
    """
    For each item in the iterable `x`, yields the position of the item in the
    list of unique values of `x`.

    >>> list(uids(["a", "b", "a", "c", "c"]))
    [0, 1, 0, 2, 2]
    """

    U = {}
    for item in x:
        if item not in U:
            U[item] = len(U)
        yield U[item]


def which(x):
    """
    Yields the indices of the items of `x` which evaluate to `True`.

    >>> list(which((True, False, True, True)))
    [0, 2, 3]

    >>> list(which((1, 0, 1.0, 0.0, "a", "", None)))
    [0, 2, 4]
    """

    for (index, item) in enumerate(x):
        if item:
            yield index


def along(x):
    """
    Yields the element number for each item in the iterable `x`.

    >>> list(along(['a', 'b', 'c']))
    [0, 1, 2]
    """

    for (nItem, item) in enumerate(x):
        yield nItem


def isnth(x, each, offset):
    """
    Generator which for each item of the iterable `x` returns `True` each n-th
    time (specified by `each`) and `False` otherwise, with an offset specified
    by `offset`.

    >>> list(isnth(range(9), 3, 1))
    [False, True, False, False, True, False, False, True, False]

    .. seealso:: :func:`dh.utils.zisnth`, :func:`dh.utils.nth` for related
                functionality.
    """

    offset = (offset % each)
    for nItem in along(x):
        yield ((nItem % each) == offset)


def zisnth(x, *args, **kwargs):
    """
    Zips :func:`dh.utils.isnth` with the original iterable `x`, similar to
    the builtin :func:`enumerate()`.

    >>> list(zisnth(range(9), 3, 1))
    [(False, 0), (True, 1), (False, 2), (False, 3), (True, 4), (False, 5), (False, 6), (True, 7), (False, 8)]

    .. seealso:: :func:`dh.utils.isnth`, :func:`dh.utils.nth` for related
                functionality.
    """

    return zip(isnth(x, *args, **kwargs), x)


def nth(*args, **kwargs):
    """
    Generator which yields each n-th item of the iterable `x` (specified by
    `each`), with an offset specified by `offset`.

    >>> list(nth(range(9), 3, 1))
    [1, 4, 7]

    .. seealso:: :func:`dh.utils.isnth`, :func:`dh.utils.zisnth` for related
                functionality.
    """

    return which(isnth(*args, **kwargs))


def ranks(x, reverse=False):
    """
    Returns a tuple containing the rank of each element of the iterable `x`.

    The ranks start at `0`. If `reverse` is `False`, the elements of `x` are
    ranked in ascending order, and in descending order otherwise.

    Equal elements will all be assigned the same (lowest-possible) rank.

    >>> ranks(["d", "a", "c", "b"])
    (3, 0, 2, 1)

    >>> ranks(["d", "a", "c", "b"], reverse=True)
    (0, 3, 1, 2)

    >>> ranks(["d", "a", "c", "b", "c"])
    (4, 0, 2, 1, 2)
    """

    s = sorted(x, reverse=reverse)
    return tuple(s.index(item) for item in x)


def powerset(x):
    """
    Generator which yields each element of the powerset of the iterable `x`.

    >>> list(powerset([1, 2, 3]))
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

    .. seealso:: http://docs.python.org/library/itertools.html#recipes
    """

    L = list(x)
    return itertools.chain.from_iterable(itertools.combinations(L, k) for k in range(len(L) + 1))


def dntup(x, n):
    """
    Return an `n`-tuple of the values of `x`. If `x` is a scalar, it is
    repeated `n` tmes.

    Useful when an `n`-tuple is needed, but the user should be able to also
    specify a scalar which is then repeated accordingly.

    >>> dntup('a', 2)
    ('a', 'a')
    >>> dntup(['a', 'b'], 2)
    ('a', 'b')
    >>> dntup(['a', 'b', 'c'], 2)
    ('a', 'b')
    >>> dntup(['a', 'b'], 5)
    ('a', 'b', 'a', 'b', 'a')
    """
    if isinstance(x, (tuple, list)):
        xTuple = tuple(x)
    else:
        xTuple = (x,)
    return tuple(cycle(xTuple, n))


###
#%% math
###


def around(number, digitCount=3):
    """
    Rounds a number to the first `digitCount` digits after the appearance of
    the first non-zero digit ("adaptive round").

    >>> around(1234.56789, 3)
    1230.0

    >>> around(0.00123456789, 3)
    0.00123
    """

    try:
        magnitude = math.floor(math.log10(abs(number)))
    except ValueError:
        magnitude = 0
    roundDigitCount = int(digitCount - magnitude - 1)
    return round(number, roundDigitCount)


def cdist(x, y):
    """
    Returns the circular distance between two points on a unit circle. The
    points `x` and `y` must be given by their angle (in degree) on the unit
    circle.

    >>> cdist(90.0, 350.0)
    100.0

    >>> cdist(90.0, 260.0)
    170.0

    >>> cdist(90.0, 280.0)
    170.0

    >>> cdist(-20.0, 270.0)
    70.0
    """

    d = x - y
    return min(d % 360, -d % 360)


def diff(x):
    """
    Yields the successive differences of the elements of `x`.

    It works for any data type that supports subtraction (e.g., also fractions
    via `fractions.Fraction`).

    >>> list(diff([1, 4, 2, 3]))
    [3, -2, 1]
    """

    last = None
    for item in x:
        if last is not None:
            yield item - last
        last = item


def cumsum(x):
    """
    Yields the cumulative sum of the elements of `x`.

    It works for any data type that supports addition (e.g., also fractions via
    `fractions.Fraction`).

    >>> list(cumsum([1, 4, 2, 3]))
    [1, 5, 7, 10]
    """

    c = None
    for item in x:
        if c is None:
            c = item
        else:
            c += item
        yield c


class odiff():
    """
    Returns the difference between the last two values that were added
    ("online difference").

    The first difference value to be returned is specified by `firstDiff`.

    >>> a = odiff(firstDiff=0)
    >>> a.update(3)
    0
    >>> a.update(7)
    4
    >>> a.update(4)
    -3
    >>> a.update(45)
    41
    """

    def __init__(self, firstDiff=None):
        self.values = [None, None]
        self.firstDiff = firstDiff
        self.first = True

    def update(self, value):
        self.values[0] = self.values[1]
        self.values[1] = value

        if self.first:
            self.first = False
            return self.firstDiff
        else:
            return self.values[1] - self.values[0]


class osum():
    """
    Returns the sum of all values that were added ("online sum").

    The starting value of the sum is specified by `start`.

    >>> s = osum()
    >>> s.update(3)
    3
    >>> s.update(7)
    10
    >>> s.update(4)
    14
    >>> s.update(45)
    59
    """

    def __init__(self, start=0):
        self.sum = start

    def update(self, value=1):
        self.sum = self.sum + value
        return self.sum


def mean(x):
    """
    Returns the mean of the elements of the iterable `x`.

    It also works for generators which have no `len`.

    >>> mean([1, 3, 2, 4, 0])
    2.0

    >>> mean(n for n in range(5))
    2.0
    """

    try:
        # check if x has `len`
        l = len(x)
    except TypeError:
        # if not, count the items explicitly
        s = None
        l = 0
        for item in x:
            if s is None:
                s = item
            else:
                s += item
            l += 1
        return s / l
    else:
        # otherwise, no need to count
        return sum(x) / l


def median(x):
    """
    Returns the median of the elements of the iterable `x`.

    If the number of elements in `x` is even, the arithmetic mean of the upper
    and lower median values is returned.

    >>> median([3, 7, 4])
    4

    >>> median([3, 7, 4, 45])
    5.5
    """

    s = sorted(x)
    N = len(s)
    if (N % 2) == 1:
        return s[(N - 1) // 2]
    else:
        M = N // 2
        return 0.5 * (s[M - 1] + s[M])


class omedian():
    """
    Returns the median of the last `nLast` values that were added ("online
    median").

    >>> m = omedian(nLast=3)
    >>> m.update(3)
    3
    >>> m.update(7)
    5.0
    >>> m.update(4)
    4
    >>> m.update(45)
    7
    >>> m.update(2)
    4
    >>> m.update(3)
    3
    """

    def __init__(self, nLast=10):
        self.values = collections.deque()
        self.nLast = nLast

    def update(self, value):
        self.values.append(value)
        if len(self.values) > self.nLast:
            self.values.popleft()
        return median(self.values)


def sclip(x, lower=None, upper=None, keepType=False):
    """
    Clips the scalar value `x` to the interval [`lower`, `upper`].

    Each of `lower` and `upper` can be `None`, meaning no clipping. If
    `keepType` is `True`, the returned result has the same type as the input
    `x`, otherwise it has either the type of `x` (if it was not clipped) or the
    type of the `lower` or the `upper` value which was used for clipping.

    >>> sclip(-123.456, 0, 100, False)
    0

    >>> sclip(-123.456, 0, 100, True)
    0.0

    >>> sclip(123.456, 0, 100, False)
    100

    >>> sclip(123.456, 0, 100, True)
    100.0
    """

    xType = type(x)
    c = x
    if lower is not None:
        c = max(lower, c)
    if upper is not None:
        c = min(upper, c)

    if keepType:
        return xType(c)
    else:
        return c


def tinterval(x, lowerOld, upperOld, lowerNew, upperNew):
    """
    Transform the scalar `x` from the interval [`lowerOld`, `upperOld`] to the
    interval [`lowerNew`, `upperNew`].

    >>> tinterval(0.5, 0.0, 1.0, 1.0, 512.0)
    256.5
    """

    return (x - lowerOld) / (upperOld - lowerOld) * (upperNew - lowerNew) + lowerNew


###
#%% formatting
###


def fhex(x, nDigits=2, prefix="0x", upper=True):
    """
    Returns a hex string of the number `x`, with a fixed number `nDigits` of
    digits, prefixed by `prefix`. If `upper` is `True`, hex digits are
    upper-case, otherwise lower-case.

    >>> fhex(15)
    '0x0F'

    >>> fhex(255, 4, "", False)
    '00ff'

    .. seealso:: http://stackoverflow.com/a/12638477/1913780
    """

    return "{prefix}{x:0{nDigits}{case}}".format(
        prefix=prefix,
        x=x,
        nDigits=nDigits,
        case="X" if upper else "x",
    )


def numerus(count, wordSingular, wordPlural=None):
    """
    Return the singular `wordSingular` or the plural form `wordPlural` of a
    noun, depending of the value of `count`.

    If `wordPlural` is `None`, it equals to `wordSingular` with an appended
    's'.

    >>> numerus(1, 'car')
    'car'

    >>> numerus(2, 'car')
    'cars'
    """

    if count == 1:
        return wordSingular
    else:
        if wordPlural is None:
            wordPlural = wordSingular + "s"
        return wordPlural


def ohash(x, outputFormat="hex", byteCount=64):
    """
    Hash any serializable object.

    `outputFormat` determines how to convert the hash output. It can be
    `'raw'` (or `'bytes'`), `'base2'` (or `'bin'`), `'base10'` (or `'int'`),
    `'base16'` (or `'hex'`), `'base32'`, or `'base64'`.
    `byteCount` specifies the number of bytes to use from the hash output. It
    must be in (1, 2, 4, 8, 16, 32, 64).

    >>> ohash({'x': 1, 'y': 'two', 'z': [3.0, None]}, 'hex', 4)
    'f2e79df1'

    >>> ohash({'x': 1, 'y': 'two', 'z': [3.0, None]}, 'int', 2)
    28438
    """

    # serialize the object and hash the serialization string (512 bits = 64 bytes)
    # note pickle.dumps is not used here as it sometimes gave different results for identical objects
    #xSerialized = pickle.dumps(x, protocol=0)
    xSerialized = pprint.pformat(x).encode("utf-8")
    hashBytes = hashlib.sha512(xSerialized).digest()

    # reduce byte count (repeatedly XOR the two halves of the byte array until the desired length is reached)
    if byteCount not in (1, 2, 4, 8, 16, 32, 64):
        raise ValueError("Invalid byte count ({}), must be in (1, 2, 4, 8, 16, 32, 64)".format(byteCount))
    while len(hashBytes) > byteCount:
        hashBytesReduced = b""
        for (int1, int2) in hzip(hashBytes):
            hashBytesReduced += (int1 ^ int2).to_bytes(1, byteorder="big", signed=False)
        hashBytes = hashBytesReduced

    # format output
    if outputFormat in ("raw", "bytes"):
        hashFormatted = hashBytes
    elif outputFormat in ("base2", "bin"):
        hashFormatted = "".join(bin(hashByte)[2:].zfill(8) for hashByte in hashBytes)
    elif outputFormat in ("base10", "int"):
        hashFormatted = int.from_bytes(hashBytes, byteorder="big", signed=False)
    elif outputFormat in ("base16", "hex"):
        hashFormatted = base64.b16encode(hashBytes).decode("ascii").lower()
    elif outputFormat in ("base32",):
        hashFormatted = base64.b32encode(hashBytes).decode("ascii")
    elif outputFormat in ("base64",):
        hashFormatted = base64.b64encode(hashBytes).decode("ascii")
    elif outputFormat in ("float", "color"):
        hashFloat = int.from_bytes(hashBytes, byteorder="big", signed=False) / 2**(8 * byteCount)
        if outputFormat in ("float",):
            hashFormatted = hashFloat
        elif outputFormat in ("color",):
            hashFormatted = colorsys.hsv_to_rgb(hashFloat, 1.0, 1.0)
    else:
        raise ValueError("Invalid output format '{}'".format(outputFormat))

    return hashFormatted


def capitalize(s):
    """
    Returns a capitalized version of the string `s`.

    >>> capitalize("test")
    'Test'

    .. seealso:: http://stackoverflow.com/a/352513/1913780
    """

    return s[:1].upper() + s[1:]


def uncolorize(s):
    """
    Remove ANSI color escape codes from the string `s` and return the result.

    Works with text colorized with the `colorama` module.
    """
    return re.sub("\033\[([0-9]+;)*[0-9]*m", "", s, flags=re.UNICODE)


def tstr(s, maxLength=80, ellipsis="..."):
    """
    Truncates the string `s` and adds ellipsis such that the returned string
    has at most `maxLength` characters, including the ellipsis.

    >>> tstr('The quick brown fox jumps over the lazy dog', 40)
    'The quick brown fox jumps over the la...'
    """

    if len(s) > maxLength:
        return s[:max(0, maxLength - len(ellipsis))] + ellipsis
    else:
        return s


def fargs(*args, **kwargs):
    """
    Format `*args` and `**kwargs` into one string resembling the original call.

    >>> fargs(1, [2], x=3.0, y='four')
    "1, [2], x=3.0, y='four'"

    .. note:: The items of `**kwargs` are sorted by their key.
    """

    items = []
    for arg in args:
        items.append(pprint.pformat(arg))
    for kw in sorted(kwargs):
        items.append(kw + "=" + pprint.pformat(kwargs[kw]))
    return ", ".join(items)


def ftime(secs):
    """
    Format a time duration `secs` given in seconds into a human readable
    string.

    >>> ftime(12345)
    '3h25m45s'
    """

    units = ("d", "h", "m", "s")
    factors = (86400, 3600, 60, 1)

    res = ""
    if secs < 0.0:
        # add sign
        secs = abs(secs)
        res += "-"
    for (unit, factor) in zip(units, factors):
        value = int(secs // factor)
        secs -= value * factor
        if (value > 0) or (unit == units[-1]):
            res += "{value}{unit}".format(value=value, unit=unit)

    return res


def dtstr(compact=True):
    """
    Returns the current timestamp string including date, time, and
    microseconds.
    """

    if compact:
        fmt = "%Y%m%d-%H%M%S-%f"
    else:
        fmt = "%Y-%m-%d %H:%M:%S.%f"
    return datetime.datetime.now().strftime(fmt)


def hnum(n):
    """
    Format number `n` as human-readable string by adding thousand-separators.

    >>> hnum(1)
    '1'

    >>> hnum(1000000)
    '1,000,000'

    >>> hnum(-123456.789)
    '-123,456.789'
    """

    return dh.thirdparty.humanize.intcomma(n)


def hfrac(n):
    """
    Format number `n` as human-readable fractional string.

    >>> hfrac(1)
    '1'

    >>> hfrac(0.3)
    '3/10'

    >>> hfrac(1.666666667)
    '1 2/3'

    >>> hfrac(12.3456789)
    '12 28/81'
    """

    return dh.thirdparty.humanize.fractional(n)


def hord(n):
    """
    Format number `n` as ordinal number string.

    >>> hord(1)
    '1st'

    >>> hord(2)
    '2nd'

    >>> hord(3)
    '3rd'

    >>> hord(11)
    '11th'

    >>> hord(23)
    '23rd'

    >>> hord(1234)
    '1234th'
    """

    return dh.thirdparty.humanize.ordinal(n)


def htime(delta):
    """
    Format time delta `delta` as human-readable string. The time delta can
    be given as numeric type (meaning seconds), or as `datetime.timedelta`.

    >>> htime(12)
    '12 seconds'

    >>> htime(135)
    '2 minutes'

    >>> htime(48 * 60 * 60)
    '2 days'

    >>> import datetime
    >>> htime(datetime.timedelta(weeks=3, days=2, hours=1))
    '23 days'

    >>> htime(123456789)
    '3 years'
    """

    return dh.thirdparty.humanize.naturaldelta(delta)


def hbytes(byteCount):
    """
    Format byte count `byteCount` as human-readable string.

    >>> hbytes(1023)
    '1023 Bytes'

    >>> hbytes(1024)
    '1.0 KiB'

    >>> hbytes(1.23 * 1024)
    '1.2 KiB'

    >>> hbytes(12.345 * 1024 * 1024 * 1024)
    '12.3 GiB'
    """

    return dh.thirdparty.humanize.naturalsize(byteCount, binary=True)


def table(*args, **kwargs):
    """
    Format an iterable of iterables or a similar construct (e.g., list of
    lists, list of dicts) into (the string of) a table.

    This function is an alias of :func:`dh.thirdparty.tabulate.tabulate()`.
    """

    return dh.thirdparty.tabulate.tabulate(*args, **kwargs)


def ptable(*args, **kwargs):
    """
    Prints the table formatted via the function :func:`dh.utils.table`.

    >>> ptable([["row1", 12.34], ["row2", 5.6789]])
    ----  -------
    row1  12.34
    row2   5.6789
    ----  -------
    """

    print(table(*args, **kwargs))


def pbar(*args, **kwargs):
    """
    Progress bar.

    This function is an alias of :func:`dh.thirdparty.tqdm.tqdm()`.
    """

    return dh.thirdparty.tqdm.tqdm(*args, **kwargs)


###
#%% file-related
###


def absdir(path):
    """
    Returns the absolute path of the directory name of `path`.
    """

    return os.path.abspath(os.path.dirname(path))


def mkdir(dirname):
    """
    Creates directory `dirname` if it does not exist already.

    .. seealso:: http://stackoverflow.com/a/5032238/1913780
    """

    if dirname == "":
        return
    try:
        os.makedirs(dirname)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def exdir(dirname):
    """
    Same as :func:`dh.utils.mkdir`, but returns the dirname after the dir was
    created.
    """

    mkdir(dirname)
    return dirname


def mkpdir(filename):
    """
    Creates the parent directory of `filename` if it does not exists already.
    """

    mkdir(os.path.dirname(filename))


def fbak(filename):
    """
    Backs up the file given by `filename` by creating a copy in the same dir,
    with a timestamp added to the filename before the file extension.
    """

    t = dtstr()
    (basename, ext) = os.path.splitext(filename)
    filenameBak = "{}.bak-{}{}".format(basename, t, ext)
    try:
        shutil.copy2(filename, filenameBak)
    except FileNotFoundError:
        pass


def bopen(file, *args, **kwargs):
    """
    Like :func:`open()`, but backs up the file before opening it.
    """

    fbak(filename=file)
    return open(file, *args, **kwargs)


def awopen(*args, **kwargs):
    """
    Like :func:`open()`, but ensures that writing is atomic.

    This function is an alias for
    :func:`dh.thirdparty.atomicwrites.atomic_write()`.
    """

    return dh.thirdparty.atomicwrites.atomic_write(*args, **kwargs)


class JsonConfigParser(configparser.ConfigParser):
    """
    ConfigParser where the config values are JSON-encoded.
    """

    def get(self, *args, **kwargs):
        return json.loads(super().get(*args, **kwargs))

    def set(self, section, option, value):
        return super().set(section=section, option=option, value=json.dumps(value))


###
#%% general helpers
###


class Fsm(dh.thirdparty.transitions.Machine):
    """
    Finite-state-machine class.

    This class is an alias of :func:`dh.thirdparty.transitions.Machine()`.
    """
    pass


def rupdate(d, u, deepcopy=True):
    """
    Performs a recursive update of the nested dict `d` with according values of
    the nested dict `u`.

    If `deepcopy` is `True`, a deep copy of `d` is updated and returned, while
    the original `d` remains unchanged.

    The difference to the builtin `dict.update` is that this also works for
    nested dicts.

    >>> d = {'a': 1, 'b': {'ba': 2, 'bb': 3}, 'c': {'ca': 4, 'cb': 5}, 'd': {'da': 6, 'db': 7}}
    >>> u = {'a': 'one', 'b': {'ba': 'two'}, 'c': 'fourfive'}
    >>> d = rupdate(d, u)
    >>> d['a']
    'one'
    >>> d['b']['ba']
    'two'
    >>> d['b']['bb']
    3
    >>> d['c']
    'fourfive'
    >>> d['d']['da']
    6
    >>> d['d']['db']
    7

    .. seealso:: http://stackoverflow.com/a/3233356/1913780
    .. seealso:: http://stackoverflow.com/a/5105554/1913780
    """

    if deepcopy:
        d = copy.deepcopy(d)

    for (key, value) in u.items():
        if isinstance(value, collections.Mapping):
            r = rupdate(d.get(key, {}), value)
            d[key] = r
        else:
            d[key] = u[key]
    return d


class avdict():
    """
    Class with (recursive) autovivification of attributes and items.

    Attributes and items of the same name refer to the same object.

    >>> d = avdict()
    >>> d.foo.bar.xyz = 123
    >>> d.foo.bar.xyz
    123
    >>> d["foo"].bar["xyz"]
    123

    >>> d = avdict(x = 1, y = 2)
    >>> d.x
    1
    """

    def __init__(self, **kwargs):
        for (key, value) in kwargs.items():
            self[key] = value

    def __getitem__(self, key):
        """
        This is where the magic happens: if an attribute does not exists, it is
        created as an instance of this class.
        """

        if key not in self.__dict__:
            self.__dict__[key] = avdict()
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, attr):
        return self[attr]

    def todict(self):
        """
        Returns a nested dictionary resembling the structure of the instance.
        """

        d = {}
        for (key, value) in self.__dict__.items():
            if isinstance(value, type(self)):
                d[key] = value.todict()
            else:
                d[key] = value
        return d


def fsched(f, diff, timeout=None, stopOnException=True, *args, **kwargs):
    """
    Simple scheduler which repeatedly calls a function `f` with a fixed time
    interval `diff` (in seconds) between calls.

    The scheduler stops when a function call evaluates to false, or when
    `stopOnException` is true and the function call triggers an exception. If
    `timeout` (in seconds) is specified, the scheduler will raise a
    `RuntimeError` if it did not stop until this point. `*args` and `**kwargs`
    are passed to `f` for each call.

    .. seealso:: `sched.scheduler` for a more flexible scheduler.
    """

    timeNow = time.time()
    timeNext = timeNow
    if timeout is not None:
        timeTimeout = timeNow + timeout
    while True:
        # timeout?
        if (timeout is not None) and (timeNext >= timeTimeout):
            raise RuntimeError("Scheduler timed out")

        # sleep until next call is due and schedule next call
        timeNow = time.time()
        timeWait = max(timeNext - timeNow, 0.0)
        time.sleep(timeWait)
        timeNext = time.time() + diff

        # call function
        try:
            res = f(*args, **kwargs)
        except:
            if stopOnException:
                raise

        # stop if the function return value evaluates to false
        if not res:
            return


###
#%% imports
###


def timport(name):
    """
    Try to import and return the module named `name`, and return `None` on
    failure.
    """

    try:
        return importlib.import_module(name)
    except ImportError:
        return None


###
#%% user interaction
###


def qkeys():
    """
    Returns a tuple of key codes ('unicode code points', as returned by
    :func:`ord()`) which correspond to key presses indicating the desire to
    quit (`<ESC>`, `q`, `Q`).

    >>> qkeys()
    (27, 113, 81)
    """

    return (27, ord("q"), ord("Q"))


###
#%% development
###


def deprecated(message):
    """
    Raise a depracation warning with the specified `message`.

    .. note:: Raised `DeprecationWarning`s are ignored by default. See
              http://stackoverflow.com/a/20960427/1913780 for details.
    """

    warnings.warn(message, DeprecationWarning, stacklevel=2)


def out(*names):
    """
    Prints the values of the variables specified by `*names`.

    >>> x = 123
    >>> abcdef = 'four'
    >>> out('x', 'abcdef')
    x .... = 123
    abcdef = 'four'

    .. warning:: Only use for debugging!
    """

    # resolve variables to get the values
    values = tuple(resolve(name) for name in names)

    # formatted output
    maxLen = max(len(name) for name in names)
    for (name, value) in zip(names, values):
        print(("{name:.<" + str(maxLen) + "} = {value}").format(name=name if len(name) == maxLen else name + " ", value=repr(value)))


def resolve(name):
    """
    Resolves the variable `name` and returns its value.

    >>> x = 123
    >>> resolve('x')
    123

    .. warning:: The lookup process is NOT identical to Python's builtin one.
                 Only use for debugging!
    """

    frame = inspect.currentframe().f_back
    while frame is not None:
        frameVars = frame.f_locals.items()
        for (varName, varValue) in frameVars:
            if varName == name:
                return varValue
        frame = frame.f_back
    raise RuntimeError("Can not resolve variable name '{name}'".format(name=name))


class Timer():
    """
    Context manager to measure the time between entering, exiting, and certain
    breakpoints ("splits").
    """

    _units = (("us", 1e-6), ("ms", 1e-3), ("s", 1.0), ("min", 60.0), ("h", 3600.0))

    def __init__(self, name=None, unit="ms"):
        self._name = name
        self._unit = unit
        for u in self._units:
            if u[0] == unit:
                self._unit = unit
                self._scale = 1.0 / u[1]
                break
        else:
            unitNames = tuple(u[0] for u in self._units)
            raise ValueError("Invalid unit name '{}', must be one of '{}'".format(unit, "', '".join(unitNames)))


    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exType, exValue, exTraceback):
        self.stop()

    def reset(self):
        self._splits = []
        self._t0 = time.time()

    def start(self):
        self.reset()
        self.split("__START__")

    def stop(self):
        self.split("__STOP__")

    def split(self, name=None):
        t = max(time.time() - self._t0, 0.0)
        if name is None:
            name = "__SPLIT_{}__".format(len(self._splits))
        self._splits.append({
            "name": name,
            "t": t,
        })

    def __str__(self):
        """
        Return a string of the measured results formatted as a table.
        """

        ts = [split["t"] for split in self._splits]
        dts = list(diff(ts))
        #dts.append(0.0)

        rows = []
        for (splitFrom, splitTo, dt) in zip(self._splits[:-1], self._splits[1:], dts):
            rows.append((
                ("" if self._name is None else "{}.".format(self._name)) + splitFrom["name"],
                 ("" if self._name is None else "{}.".format(self._name)) + splitTo["name"],
                dt * self._scale,
                splitTo["t"] * self._scale,
            ))
        return table(rows, headers=("From", "To", "Duration [{}]".format(self._unit), "Cumulative [{}]".format(self._unit)))


class FrequencyEstimator():
    def __init__(self, minKeepCount=10, minKeepTime=1.0):
        self.minKeepCount = minKeepCount
        self.minKeepTime = minKeepTime
        self._ts = [time.time()]

    def event(self):
        # save event time
        self._ts.append(time.time())

        # clean entries which exceed both the minKeepCount and the minKeepTime
        for nTime in range(len(self._ts) - self.minKeepCount, -1, -1):
            if self._ts[nTime] + self.minKeepTime < self._ts[-1]:
                break
        else:
            nTime = None
        if nTime is not None:
            self._ts = self._ts[nTime:]

        # return events per second as float
        if len(self._ts) <= 1:
            return 0.0
        else:
            return (len(self._ts) - 1) / (self._ts[-1] - self._ts[0])


def _pdeco(callerName, fName, message):
    """
    Formats and prints a message, designed to be used by decorator functions
    such as :func:`dh.utils.pentex`, :func:`dh.utils.pargs`, etc.
    """

    print(
        "==> @{callerName}({fName}){spaces}  --  {message}".format(
            callerName=callerName,
            spaces=" " * max(0, 8 - len(callerName)),
            fName=fName,
            message=message
        )
    )


def pentex(f):
    """
    Decorator which prints a message when entering and exiting `f`.

    >>> @pentex
    ... def f(x): return x**2
    >>> res = f(2)
    ==> @pentex(f)    --  enter
    ==> @pentex(f)    --  exit
    """

    @functools.wraps(f)
    def g(*args, **kwargs):
        _pdeco("pentex", f.__name__, "enter")
        ret = f(*args, **kwargs)
        _pdeco("pentex", f.__name__, "exit")
        return ret

    return g


def ptdiff(f):
    """
    Decorator which prints the time difference between entering and exiting
    `f`.
    """

    @functools.wraps(f)
    def g(*args, **kwargs):
        t0 = time.time()
        ret = f(*args, **kwargs)
        t1 = time.time()
        _pdeco("ptdiff", f.__name__, "{dt} seconds".format(
            dt=around(max(0, t1 - t0), 3)
        ))
        return ret

    return g


def pargs(f):
    """
    Decorator which prints the arguments supplied to `f`.

    >>> @pargs
    ... def f(x, y): return x * y
    >>> res = f(2, y=3)
    ==> @pargs(f)     --  (2, y=3)

    .. todo:: truncate each argument value individually (otherwise an image
              array as first argument masks all other arguments)
    """

    @functools.wraps(f)
    def g(*args, **kwargs):
        _pdeco("pargs", f.__name__, "({argstr})".format(
            argstr=tstr(fargs(*args, **kwargs), 120, "<... truncated>"),
        ))
        return f(*args, **kwargs)

    return g


def parghash(f):
    """
    Decorator which prints the hash value (using :func:`dh.utils.ohash`) of the
    arguments supplied to `f`.

    >>> @parghash
    ... def f(x, y): return x * y
    >>> res = f(2, y=3)
    ==> @parghash(f)  --  5cd54cfc
    """

    @functools.wraps(f)
    def g(*args, **kwargs):
        _pdeco("parghash", f.__name__, "{arghash}".format(
            arghash=ohash((args, kwargs), "hex", 4)
        ))
        return f(*args, **kwargs)

    return g


def pret(f):
    """
    Decorator which prints the result returned by `f`.

    >>> @pret
    ... def f(x, y): return {'sum': x + y, 'prod': x * y}
    >>> res = f(2, 3)
    ==> @pret(f)      --  {'prod': 6, 'sum': 5}
    """

    @functools.wraps(f)
    def g(*args, **kwargs):
        ret = f(*args, **kwargs)
        _pdeco("pret", f.__name__, "{retstr}".format(
            retstr=tstr(pprint.pformat(ret), 120, "<... truncated>"),
        ))
        return ret

    return g


def prethash(f):
    """
    Decorator which prints the hash value (using :func:`dh.utils.ohash`) of the
    result returned by `f`.

    >>> @prethash
    ... def f(x, y): return {'sum': x + y, 'prod': x * y}
    >>> res = f(2, 3)
    ==> @prethash(f)  --  3e4601af
    """

    @functools.wraps(f)
    def g(*args, **kwargs):
        ret = f(*args, **kwargs)
        _pdeco("prethash", f.__name__, "{rethash}".format(
            rethash=ohash(ret, "hex", 4)
        ))
        return ret

    return g


def pall(f):
    """
    Decorator which applies the :func:`dh.utils.pentex`,
    :func:`dh.utils.pargs`, :func:`dh.utils.pret`, and :func:`dh.utils.ptdiff`
    decorators on `f`.
    """

    @pentex
    @ptdiff
    @prethash
    @pret
    @pargs
    @parghash
    @functools.wraps(f)
    def g(*args, **kwargs):
        return f(*args, **kwargs)
    return g
