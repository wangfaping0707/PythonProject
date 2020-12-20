"""
Provides/handles data (e.g., images, colormaps, text files, etc.).
"""

import glob
import json
import os.path

# paths into which setup.py installs all data files
_DATA_DIR = os.path.abspath(os.path.dirname(__file__))
_COLORMAP_DIR = os.path.join(_DATA_DIR, "colormaps")
_ICON_DIR = os.path.join(_DATA_DIR, "icons")
_IMAGE_DIR = os.path.join(_DATA_DIR, "images")


###
#%% helpers
###


def _loadNpy(filename):
    import numpy as np
    return np.load(filename)


def _loadNpz(filename):
    import numpy as np
    X = np.load(filename)
    return X[list(X.keys())[0]]


###
#%% general data
###


def M(rows=3, columns=4):
    """
    Simple NumPy test matrix.

    The returned matrix is of size `rows`x`columns` and contains the integers
    from 0 to (`rows` * `columns` - 1).
    """
    import numpy as np
    return np.array(range(rows * columns)).reshape((rows, columns))


###
#%% colormaps
###


def colormap(c):
    """
    If `c` is a dict, it is assumed to be a valid colormap (see below) and is
    returned. Otherwise, `c` is interpreted as colormap name (not as filename)
    and is loaded from the colormap dir.

    A colormap is a dict, where the keys are 8 bit unsigned gray values which
    are mapped to 8 bit unsigned 3-tuples (RGB) each.
    """

    if isinstance(c, dict):
        # `c` is already a dict and assumed to be a valid colormap
        m = c
    else:
        # `c` is interpreted as colormap name, and the dict is loaded from the colormap dir
        filename = os.path.join(_COLORMAP_DIR, "{}.{}".format(c.lower(), "json"))
        with open(filename, "r") as f:
            m = json.load(f)

    # json stores dict keys as strings, so we must convert them to ints
    return {int(key): tuple(value) for (key, value) in m.items()}


def colormaps():
    """
    Returns a dict of all available colormaps. The keys are the colormap names.
    """

    filenames = glob.glob(os.path.join(_COLORMAP_DIR, "*.json"))
    names = list(sorted(os.path.splitext(os.path.basename(filename))[0] for filename in filenames))
    return {name: colormap(name) for name in names}


###
#%% image data
###


def grid(shape=(500, 500), d=25, w=1, dtype="uint8"):
    """
    Returns a binary image of size `shape` containing a regular grid with a
    distance `d` between grid lines of width `w`.

    >>> grid()[0, 0]
    255
    >>> grid()[1, 1]
    0
    """

    import numpy as np
    import dh.image

    # empty image
    (typeMin, typeMax) = dh.image.trange(dtype)
    G = np.empty(shape=shape, dtype=dtype)
    G[:, :] = typeMin

    # create grid
    for x in range(0, shape[1], d):
        G[:, x:(x+w)] = typeMax
    for y in range(0, shape[0], d):
        G[y:(y+w), :] = typeMax

    return G


def checkerboard(shape=(500, 500), d=25, low=0, high=255):
    """
    Returns a gray-scale image of size `shape` containing a checkerboard grid
    with squares of size `d`. The arguments `low` and `high` specify the gray
    scale values to be used for the squares.

    >>> checkerboard()[0, 0]
    0
    >>> checkerboard()[0, 25]
    255
    >>> checkerboard()[25, 25]
    0
    """

    import numpy as np

    C = np.zeros(shape=shape, dtype="uint8") + low
    for (nRow, y) in enumerate(range(0, shape[0], d)):
        offset = d if ((nRow % 2) == 0) else 0
        for x in range(offset, shape[1], 2 * d):
            C[y:(y + d), x:(x + d)] = high

    return C


def background(shape=(500, 500), d=25):
    """
    Returns a gray-scale image of size `shape` containing a checkerboard grid
    of light and dark gray squares of size `d`.

    >>> background()[0, 0]
    80
    >>> background()[0, 25]
    120
    >>> background()[25, 25]
    80
    """
    return checkerboard(shape=shape, d=d, low=80, high=120)


def lena():
    """
    The famous Lena image, widely used in image processing.

    Source: The USC-SIPI Image Database (http://sipi.usc.edu/database/).
    """

    return _loadNpz(os.path.join(_IMAGE_DIR, "lena.npz"))


def pal():
    """
    PAL image (Philips PM5544 test card).

    Source:
    https://commons.wikimedia.org/wiki/File:PM5544_with_non-PAL_signals.png.
    The image is released into the public domain.
    """

    return _loadNpz(os.path.join(_IMAGE_DIR, "pal.npz"))


###
#%% icons
###


def ionfn(name):
    """
    Returns the absolute path to the Ion Icon identified by `name` (which must
    be given without extension).
    """
    filename = os.path.abspath(os.path.join(_ICON_DIR, "ionicons", "png", "512", "{}.png".format(name)))
    if not os.path.exists(filename):
        raise FileNotFoundError("Icon file '{}' does not exist".format(filename))
    return filename
