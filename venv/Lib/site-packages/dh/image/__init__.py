"""
Functions for image handling, image processing, and computer vision.

All images are represented as NumPy arrays (in the form `I[y, x]` for gray
scale images and `I[y, x, channel]` for color images, with RGB channel order),
and so NumPy (but only NumPy) is required for this module. Image-related
functions which require further thirdparty modules (e.g., OpenCV, scikit-image,
mahotas, PIL) are optional.
"""

import collections
import os.path

import numpy as np

import dh.data
import dh.gui
import dh.utils


###
#%% optional thirdparty modules
###


# try to import OpenCV
try:
    import cv2
    _CV2_VERSION = cv2.__version__
    _CV2_ERROR = None
except ImportError as e:
    _CV2_VERSION = None
    _CV2_ERROR = e


# decorator for functions that need OpenCV
def CV2(f):
    def g(*args, **kwargs):
        if _CV2_VERSION is None:
            raise RuntimeError("Module 'cv2' is needed for that operation ('{}'), but could not be imported (error: {})".format(f.__name__, _CV2_ERROR))
        return f(*args, **kwargs)

    return g


# skimage
# mahotas


###
#%% input & output
###


def imread(*args, **kwargs):
    dh.utils.deprecated("'imread' is deprecated, use 'load' instead")
    return load(*args, **kwargs)


@CV2
def load(filename, color=None):
    """
    Load image from file `filename` and return NumPy array.

    If `color` is `None`, the image is loaded as-is. If `color` is `False`, a
    grayscale image is returned. If `color` is `True`, then a color image is
    returned (in RGB order), even if the original image is grayscale.

    The bit-depth (8 or 16 bit) of the image file will be preserved.

    .. note: If a color image is loaded using `color=False`, the conversion to
             gray scale will be performed by OpenCV, and the result will be
             different to first loading the image in color mode and then using
             `dh.image.asgray`.
    """

    # check if file exists
    if not os.path.exists(filename):
        raise FileNotFoundError("Image file '{}' does not exist".format(filename))

    # flags - select grayscale or color mode
    if color is None:
        flags = cv2.IMREAD_UNCHANGED
    else:
        flags = cv2.IMREAD_ANYDEPTH | (cv2.IMREAD_COLOR if color else cv2.IMREAD_GRAYSCALE)

    # read image
    I = cv2.imread(filename=filename, flags=flags)

    # BGR -> RGB
    if dh.image.iscolor(I):
        I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)

    return I


@CV2
def decode(b, color=None):
    """
    Load image from the byte array `b` containing the *encoded* image and
    return NumPy array.

    .. seealso:: `dh.image.load()` for details.
    """

    # flags - select grayscale or color mode
    if color is None:
        flags = cv2.IMREAD_UNCHANGED
    else:
        flags = cv2.IMREAD_ANYDEPTH | (cv2.IMREAD_COLOR if color else cv2.IMREAD_GRAYSCALE)

    # read image
    n = np.fromstring(b, dtype="uint8")
    I = cv2.imdecode(buf=n, flags=flags)

    # BGR -> RGB
    if dh.image.iscolor(I):
        I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)

    return I


def imwrite(*args, **kwargs):
    dh.utils.deprecated("'imwrite' is deprecated, use 'save' instead")
    return save(*args, **kwargs)


@CV2
def save(filename, I, mkpdir=True):
    """
    Write image `I` to file `filename`.

    If `mkpdir` is `True`, the parent dir of the given filename is created
    before saving the image.
    """

    if not isinstance(I, np.ndarray):
        raise RuntimeError("Invalid image (type '{}')".format(type(I).__name__))

    # create parent dir
    if mkpdir:
        dh.utils.mkpdir(filename)

    # BGR -> RGB
    if iscolor(I):
        J = I[:, :, ::-1]
    else:
        J = I

    # write
    return cv2.imwrite(filename=filename, img=J)


###
#%% visualization
###


def imshow(*args, **kwargs):
    dh.utils.deprecated("'imshow' is deprecated, use 'show' instead")
    return show(*args, **kwargs)


@CV2
def show(I, wait=0, scale=None, normalize=None, invert=False, colormap=None, windowName="show", closeWindow=False, engine=None, **kwargs):
    """
    Show image `I` on the screen.

    If `I` is a list of images, they are auto-stacked via `dh.image.astack()`.
    If `I` is a list of lists of images, they are stacked via
    `dh.image.stack()`. Otherwise, `I` is used as is.
    """

    if isinstance(I, np.ndarray):
        # I is an image, use it as it is
        J = I
    elif isinstance(I, (list, tuple)) and (len(I) > 0) and isinstance(I[0], np.ndarray):
        # I is a list of images: auto-stack them into one image
        J = astack(I)
    elif isinstance(I, (list, tuple)) and (len(I) > 0) and isinstance(I[0], (list, tuple)) and (len(I[0]) > 0) and isinstance(I[0][0], np.ndarray):
        # I is a list of lists of images: stack them into one image
        J = stack(I)
    else:
        raise ValueError("Invalid value for parameter `I` ({}) - it must be an image, a non-empty list of images or a non-empty list of non-empty lists of images".format(I))

    # normalize intensity values
    if normalize is not None:
        J = dh.image.normalize(J, mode=normalize, **kwargs)

    # convert to 8 bit
    J = convert(J, "uint8")

    # resize image
    if scale is None:
        # try to find a good scale factor automatically
        (W, H) = dh.gui.screenres()
        if (W is not None) and (H is not None):
            scale = 0.85 * min(H / J.shape[0], W / J.shape[1])
        else:
            scale = 850.0 / max(I.shape)
    J = resize(J, scale)

    # invert
    if invert:
        J = dh.image.invert(J)

    # apply colormap
    if colormap is not None:
        J = colorize(asgray(J), c=colormap)

    # determine how to display the image
    if engine is None:
        # TODO: auto-detect if in notebook, then use IPython as engine
        engine = "cv2"

    if engine == "cv2":
        # RGB -> BGR (for OpenCV)
        if iscolor(J):
            J = J[:,:,::-1]
        cv2.imshow(windowName, J)
        key = cv2.waitKey(wait)
        if closeWindow:
            cv2.destroyWindow(windowName)
    elif engine == "ipython":
        # source: https://gist.github.com/uduse/e3122b708a8871dfe9643908e6ef5c54
        import PIL.Image
        from io import BytesIO
        import IPython.display
        f = BytesIO()
        PIL.Image.fromarray(J).save(f, "png")
        IPython.display.display(IPython.display.Image(data=f.getvalue()))
        key = 0
    else:
        raise RuntimeError("Unsupported engine '{}'".format(engine))

    return key


def stack(Is, padding=0, dtype=None, gray=None):
    """
    Stack images given by `Is` into one image.

    `Is` must be a vector of images (in which case the images are stacked
    horozontally) or a vector of vectors of images, defining rows and columns.
    """

    if isinstance(Is[0], np.ndarray):
        rows = [Is]
    elif isinstance(Is[0][0], np.ndarray):
        rows = Is
    else:
        raise ValueError("Invalid argument 'Is' - must be vector of images or vector of vectors of images")

    # find common data type and color mode
    if dtype is None:
        dtype = tcommon((I.dtype for row in rows for I in row))
    if gray is None:
        gray = all(isgray(I) for row in rows for I in row)

    # step 1/2: construct stacked image for each row
    Rs = []
    width = 0
    for (nRow, row) in enumerate(rows):
        # height of the row
        rowHeight = 0
        for I in row:
            rowHeight = max(rowHeight, I.shape[0])
        if nRow == 0:
            rowHeight += 2 * padding
        else:
            rowHeight += padding

        R = None
        for (nCol, I) in enumerate(row):
            # convert to common data type and color mode
            if gray:
                J = asgray(I)
            else:
                J = ascolor(I)
            J = convert(J, dtype)

            # add padding
            p = [[padding if nRow == 0 else 0, padding], [padding if nCol == 0 else 0, padding]]
            if not gray:
                p.append([0, 0])
            J = np.pad(J, p, mode="constant", constant_values=0)

            # ensure that image has the height of the row
            gap = rowHeight - J.shape[0]
            if gap > 0:
                if gray:
                    Z = np.zeros(shape=(gap, J.shape[1]), dtype=dtype)
                else:
                    Z = np.zeros(shape=(gap, J.shape[1], 3), dtype=dtype)
                J = np.vstack((J, Z))

            # add to current row image
            if R is None:
                R = J
            else:
                R = np.hstack((R, J))

        width = max(width, R.shape[1])
        Rs.append(R)

    # step 2/2: construct stacked image from the row images
    S = None
    for R in Rs:
        # ensure that the row image has the width of the final image
        gap = width - R.shape[1]
        if gap > 0:
            if gray:
                Z = np.zeros(shape=(R.shape[0], gap), dtype=dtype)
            else:
                Z = np.zeros(shape=(R.shape[0], gap, 3), dtype=dtype)
            R = np.hstack((R, Z))

        # add to final image
        if S is None:
            S = R
        else:
            S = np.vstack((S, R))

    return S


def astack(Is, padding=0, dtype=None, gray=None, aspect=1.77):
    """
    Given a 1d image list `Is`, returns a 2d-stacked image with an aspect ratio
    as close as possible to the desired aspect ratio `aspect`.
    """

    # find the optimal image count per row
    imageCount = len(Is)
    bestImageCountPerRow = 1
    bestError = float("inf")
    for imageCountPerRow in range(1, imageCount + 1):
        H = 0
        W = 0
        nImageRow = 0
        rowH = 0
        rowW = 0
        for (nImage, I) in enumerate(Is):
            rowH = max(rowH, I.shape[0] + padding)
            rowW += I.shape[1] + padding
            if ((nImageRow + 1) == imageCountPerRow) or ((nImage + 1) == imageCount):
                H += rowH
                W = max(W, rowW)
                nImageRow = 0
                rowH = 0
                rowW = 0
            else:
                nImageRow += 1
        H += padding
        W += padding

        error = abs(aspect - (W / H))
        if error < bestError:
            bestImageCountPerRow = imageCountPerRow
            bestError = error

    # construct 2d list of images
    rows = []
    row = []
    for (nImage, I) in enumerate(Is):
        row.append(I)
        if (len(row) == bestImageCountPerRow) or ((nImage + 1) == imageCount):
            rows.append(row)
            row = []

    return stack(Is=rows, padding=padding, dtype=dtype, gray=gray)


@CV2
def text(I, message, font="sans", scale=1.0, position=(0.0, 0.0), anchor="lt", padding=1.0):
    """
    Draws the text `message` into the image `I`.

    The `position` is given as 2D point in relative coordinates (i.e., with
    coordinate ranges of [0, 1]). The `anchor` must be given as two letter
    string,  following the pattern `[lcr][tcb]`. It specifies the horizontal
    and vertical alignment of the text with respect to the given position. The
    `padding` is given in (possibly non-integer) multiples of the font's
    baseline height.
    """

    # font
    if font == "sans":
        fontFace = cv2.FONT_HERSHEY_DUPLEX
    elif font == "serif":
        fontFace = cv2.FONT_HERSHEY_TRIPLEX
    else:
        raise ValueError("Invalid font '{}'".format(font))
    fontScale = scale
    fontThickness = 1

    # calculate width and height of the text
    ((W, H), baseline) = cv2.getTextSize(
        text=message,
        fontFace=fontFace,
        fontScale=fontScale,
        thickness=fontThickness,
    )

    # base offset derived from the specified position
    offset = np.array([
        dh.utils.tinterval(position[0], 0.0, 1.0, 0, I.shape[1]),
        dh.utils.tinterval(position[1], 0.0, 1.0, 0, I.shape[0] - baseline),
    ])

    # add padding to offset
    padding = round(padding * baseline)

    # adjust offset based on the specified anchor type
    if not (isinstance(anchor, str) and (len(anchor) == 2) and (anchor[0] in ("l", "c", "r")) and (anchor[1] in ("t", "c", "b"))):
        raise ValueError("Argument 'anchor' must be a string of length two (pattern: '[lcr][tcb]') , but is '{}'".format(anchor))
    (anchorH, anchorV) = anchor
    if anchorH == "l":
        pass
    elif anchorH == "c":
        offset[0] -= W * 0.5
    elif anchorH == "r":
        offset[0] -= W
    if anchorV == "t":
        offset[1] += H
    elif anchorV == "c":
        offset[1] += H * 0.5
    elif anchorV == "b":
        pass

    offset = dh.image.tir(offset)
    I[max(0, offset[1] - H - padding):min(I.shape[0], offset[1] + max(baseline, padding)), max(0, offset[0] - padding):min(I.shape[1], offset[0] + W + padding), ...] = 0

    # draw text
    cv2.putText(
        img=I,
        text=message,
        org=offset,
        fontFace=fontFace,
        fontScale=fontScale,
        color=(255, 255, 255),
        thickness=fontThickness,
        lineType=cv2.LINE_8,
        bottomLeftOrigin=False,
    )

    return I


###
#%% data type and color mode handling
###


def eqtype(I, J):
    """
    Ensure that `I` and `J` have the same NumPy type.

    If both images have the same type, returns the type name as string.
    Otherwise, a `ValueError` is raised.
    """

    if I.dtype != J.dtype:
        raise ValueError("Images have different NumPy types ('{}', '{}')".format(I.dtype, J.dtype))
    else:
        return I.dtype


def tcommon(dtypes):
    """
    For a given vector `dtypes` of types, returns the type which supports
    all ranges.

    >>> tcommon(['bool', 'uint8', 'uint16'])
    'uint16'
    >>> tcommon(['uint8', 'bool'])
    'uint8'
    >>> tcommon(['uint8', 'uint8'])
    'uint8'
    >>> tcommon(['uint8', 'uint16'])
    'uint16'
    >>> tcommon(['uint8', 'float'])
    'float'
    """

    hierarchy = ("bool", "uint8", "uint16", "float")
    maxIndex = 0
    for dtype in dtypes:
        try:
            index = hierarchy.index(dtype)
        except ValueError:
            raise RuntimeError("Invalid image type '{dtype}'".format(dtype=dtype))
        maxIndex = max(maxIndex, index)

    return hierarchy[maxIndex]


def trange(dtype):
    """
    Returns the range (min, max) of valid intensity values for an image of
    NumPy type string `dtype`.

    Allowed types are `'bool'`, `'uint8'`, `'uint16'`, and any float type
    (e.g., `'float32'`, `'float64'`). The range for each data types follows the
    convention of the OpenCV library.

    >>> trange('uint8')
    (0, 255)
    >>> trange('float32')
    (0.0, 1.0)
    """

    if dtype is None:
        # np.issubdtype(None, "float") is True, therefore we have to check for this error here explicitly
        raise ValueError("Invalid image type '{dtype}'".format(dtype=dtype))
    elif dtype == "bool":
        return (False, True)
    elif dtype == "uint8":
        return (0, 255)
    elif dtype == "uint16":
        return (0, 65535)
    elif np.issubdtype(dtype, "float"):
        return (0.0, 1.0)
    else:
        raise ValueError("Invalid image type '{dtype}'".format(dtype=dtype))


def convert(I, dtype):
    """
    Converts image `I` to NumPy type given by the string `dtype` and scales the
    intensity values accordingly.

    Intensity values are always clipped to the allowed range (even for
    identical source and target types). Returns always a copy of the data, even
    for equal source and target types.
    """

    # clip image against its source dtype (important for floats)
    (tLower, tUpper) = trange(I.dtype)
    J = clip(I, tLower, tUpper)

    if I.dtype == dtype:
        return J
    else:
        scale = trange(dtype)[1] / trange(I.dtype)[1]
        return (J.astype("float") * scale).astype(dtype)


def nchannels(I):
    """
    Return the number of color channels of the image `I`.
    """

    D = len(I.shape)
    if D == 2:
        return 1
    elif D == 3:
        return I.shape[-1]
    else:
        raise ValueError("Unrecognized image array shape {}".format(I.shape))


def isgray(I):
    """
    Returns true if the image `I` is in gray-scale mode (i.e., if it has one
    color channel).
    """

    return (nchannels(I) == 1)


def iscolor(I):
    """
    Returns true if the image `I` is in color mode (i.e., if it has three
    color channels).
    """

    return (nchannels(I) == 3)


def asgray(I):
    """
    Convert image `I` to gray-scale mode.
    """

    if isgray(I):
        # nothing to convert, just make sure that the image shape is consistent
        D = len(I.shape)
        if D == 2:
            return I
        elif D == 3:
            return I[:, :, 0]
    else:
        return np.mean(I, axis=2).astype(I.dtype)


def ascolor(I):
    """
    Convert image `I` to color (RGB) mode.
    """

    if iscolor(I):
        # nothing to convert
        return I
    else:
        return np.dstack((I,) * 3)


def colormap(*args, **kwargs):
    dh.utils.deprecated("'dh.image.colormap' is deprecated, use 'dh.data.colormap' instead")
    return dh.data.colormap(*args, **kwargs)


def colormaps(*args, **kwargs):
    dh.utils.deprecated("'dh.image.colormaps' is deprecated, use 'dh.data.colormaps' instead")
    return dh.data.colormaps(*args, **kwargs)


def colorize(I, c="jet", reverse=False, bitwise=False):
    """
    Colorize image `I` according to the colormap `c` and return 8 bit image.

    `c` can either be a colormap dict or a colormap name, see
    :func:`dh.image.colormap`.

    .. seealso:: :func:`dh.image.colormap` for how to specify `c`
    """

    # make sure that the input has only two dimensions
    # it could also have three dimensions, with the length of the last
    # dimension being one
    J = asgray(I).copy()

    # convert input to dtype "uint8"
    J = convert(J, "uint8")

    if reverse:
        J = invert(J)

    # mapping from source (one channel) to target (three channel) color
    m = dh.data.colormap(c)

    # empty color image
    C = ascolor(np.zeros_like(J))

    # apply mapping defined by colormap dict
    for source in range(256):
        # get color
        if source in m:
            target = m[source]
        else:
            target = (0, 0, 0)

        # apply color
        if bitwise:
            M = ((J & source) > 0)
        else:
            M = (J == source)
        for nChannel in range(3):
            C[:,:,nChannel][M] = target[nChannel]

    return C


def cdemo(I=None):
    """
    Interactive demo which lets the user cycle through all available colormaps,
    applied on the given image `I`.

    Keys `+` and `-` navigate forwards and backwards (with cycling), and `q`
    quits the demo. If no image is given, a test image is used.
    """

    if I is None:
        I = np.array(list(range(256)) * 256, dtype="uint8")
        I.shape = (256, 256)
        I = resize(I, 2.0)

    cs = colormaps()
    names = sorted(cs.keys())
    colormapCount = len(names)
    if colormapCount == 0:
        raise RuntimeError("Found no colormaps")

    nColormap = 0
    run = True
    while run:
        name = names[nColormap]
        C = colorize(I, c=cs[name])
        text(C, "{}/{}: {}".format(nColormap + 1, colormapCount, name))
        while True:
            needsUpdate = True

            key = show(C, wait=10)
            if key in dh.utils.qkeys():
                run = False
            elif key in (ord("+"),):
                nColormap = (nColormap + 1) % colormapCount
            elif key in (ord("-"),):
                nColormap = (nColormap - 1) % colormapCount
            else:
                needsUpdate = False

            if needsUpdate:
                break



###
#%% pixel-wise operations
###


def identity(I):
    """
    Returns the input image `I`.

    This function is useful in image processing pipelines, in cases where a
    no-op is needed.
    """

    return I


def invert(I):
    """
    Inverts the intensities of all pixels.
    """

    (_, typeMax) = trange(I.dtype)
    return (typeMax - I)


def log(I, normalization="minmax", **kwargs):
    """
    Perform the logarithm transform to the pixel intensities of the image `I`.
    """

    (typeMin, _) = trange(I.dtype)

    J = I.copy()
    J[J == typeMin] = typeMin + 1
    F = convert(J, "float")
    L = np.log(F)
    N = normalize(L, mode=normalization, **kwargs)
    return convert(N, I.dtype)


def gamma(I, gamma, inverse=False):
    """
    Perform power-law conversion with exponent `gamma` (or one over `gamma` if
    `inverse` is true) of the intensities of image `I`.
    """

    exponent = gamma if not inverse else (1.0 / gamma)
    F = convert(I, "float")
    G = np.power(F, exponent)
    return convert(G, I.dtype)


def threshold(I, theta, relative=False):
    """
    Apply the absolute threshold `theta` to the image `I`.

    If `relative` is true, the threshold is multiplied by the maximum possible
    value for the given image type.
    """

    (typeMin, typeMax) = trange(I.dtype)
    if relative:
        theta *= typeMax
    T = I.copy()
    T[I <= theta] = typeMin
    T[I > theta] = typeMax
    return T


def clip(I, lower=None, upper=None):
    """
    Clips the image pixel values to the interval [`lower`, `upper`], and
    preserves the image type.

    Always returns a copy of the data, even if both interval ends are `None`.
    """

    J = I.copy()
    dtype = J.dtype
    (tLower, tUpper) = trange(dtype)
    if lower is not None:
        J = np.maximum(J, np.array((dh.utils.sclip(lower, tLower, tUpper),), dtype=dtype))
    if upper is not None:
        J = np.minimum(J, np.array((dh.utils.sclip(upper, tLower, tUpper),), dtype=dtype))
    return J


def normalize(I, mode="minmax", **kwargs):
    """
    Normalizes the intensity values of the image `I`.

    .. seealso:: :func:`dh.image.trange` for allowed image data types.
    """

    if mode == "none":
        return I

    elif mode == "interval":
        # interval range to be spread out to the "full" interval range
        (lower, upper) = sorted((kwargs["lower"], kwargs["upper"]))

        # the "full" interval range depends on the image's data type
        (lowerFull, upperFull) = trange(I.dtype)

        # we temporarily work with a float image (because values outside of
        # the target interval can occur)
        T = I.astype("float").copy()

        # spread the given interval to the full range, clip outlier values
        T = dh.utils.tinterval(T, lower, upper, lowerFull, upperFull)
        T = np.clip(T, a_min=lowerFull, a_max=upperFull, out=T)

        # return an image with the original data type
        return T.astype(I.dtype)

    elif mode == "minmax":
        return normalize(I, mode="interval", lower=np.min(I), upper=np.max(I))

    elif mode == "zminmax":
        # "zero-symmetric" minmax (makes only sense for float images)
        absmax = max(np.abs(np.min(I)), np.abs(np.max(I)))
        return normalize(I, mode="interval", lower=-absmax, upper=absmax)

    elif mode == "percentile":
        # get percentile
        try:
            q = float(kwargs["q"])
        except KeyError:
            q = 2.0
        q = dh.utils.sclip(q, 0.0, 50.0)
        return normalize(I, mode="interval", lower=np.percentile(I, q), upper=np.percentile(I, 100.0 - q))

    else:
        raise ValueError("Invalid mode '{mode}'".format(mode=mode))


###
#%% geometric transformations
###


@CV2
def resize(I, scale):
    """
    Resize the image `I` by a factor of `scale`, while keeping the original
    aspect ratio.

    If `scale` is smaller than `1.0`, cubic interpolation is used, otherwise
    nearest-neighbor interpolation.
    """

    interpolationType = cv2.INTER_CUBIC if (scale < 1.0) else cv2.INTER_NEAREST
    return cv2.resize(I, None, None, scale, scale, interpolationType)


def shift(I, dx=0, dy=None):
    """
    Shifts the pixels of the image `I` by `dx` and `dy` along the x and y axes.

    For each of `dx` and `dy`: if the value is an integer, it is interpreted
    as the number of pixels by which to shift. If the value is a float, it is
    interpreted as fraction of the image shape of the according axis.
    """

    # by default dy is equal to dx
    if dy is None:
        dy = dx

    # float values are interpreted as fractions of the image shape
    if isinstance(dx, float):
        dx = int(I.shape[1] * dx)
    if isinstance(dy, float):
        dy = int(I.shape[0] * dy)

    # shift
    S = I.copy()
    S = np.roll(S, dy, axis=0)
    S = np.roll(S, dx, axis=1)
    return S


def rotate(I, degree):
    """
    Rotate the image `I` counter-clock-wise by the angle specified by `degree`.

    Valid values for the angle are `0`, `90`, `180`, and `270`.
    """

    degree = int(degree) % 360
    if degree not in (0, 90, 180, 270):
        raise ValueError("Unsupported rotation angle")
    k = degree // 90
    if k > 0:
        return np.rot90(I, k)
    else:
        return I


###
#%% coordinates
###


def tir(*args):
    """
    The items of `*args` are flattened (via :func:`dh.utils.flatten`), rounded,
    converted to `int` and combined into a tuple.

    The primary use-case of this function is to pass point coordinates to
    certain OpenCV functions. It also works for NumPy arrays.

    >>> tir(1.24, -1.87)
    (1, -2)
    >>> tir([1.24, -1.87, 3.23])
    (1, -2, 3)
    """

    items = dh.utils.flatten(*args)
    return tuple(int(round(item)) for item in items)


def tirr(*args):
    """
    As :func:`dh.sci.tir`, but reverses the order of the items.

    When used to pass point coordinates to certain OpenCV functions, the item
    reversal means reversing the order of the axes (x,y -> y,x).

    >>> tirr(1.24, -1.87)
    (-2, 1)
    >>> tirr([1.24, -1.87, 3.23])
    (3, -2, 1)
    """

    items = dh.utils.flatten(*args)
    return tir(reversed(list(items)))


def hom(x):
    """
    Transforms `x` from Euclidean coordinates into a NumPy array of homogeneous
    coordinates.

    >>> hom([1.24, -1.87])
    array([ 1.24, -1.87,  1.  ])
    """

    return np.append(np.array(x), 1.0)


def unhom(x):
    """
    Transforms `x` from homogeneous coordinates into a NumPy array of Euclidean
    coordinates.

    >>> unhom([0.62 , -0.935,  0.5])
    array([ 1.24, -1.87])
    """

    return np.array(x[:-1]) / x[-1]


def hommap(M, x):
    """
    Transforms `x` to homogeneous coordinates, applies the linear mapping given
    by the matrix `M` and converts the result back to Euclidean coordinates.

    >>> M = np.eye(3)
    >>> M[0, 2] = 1.0
    >>> M[1, 2] = -2.0
    >>> hommap(M, [1.24, -1.87])
    array([ 2.24, -3.87])
    """

    return unhom(np.dot(M, hom(x)))


###
#%% frequency domain
###


def selffiltering():
    raise NotImplementedError("TODO")


###
#%% image-image operations
###


def imdiff(I, J):
    """
    Clipped image subtraction `I - J`.

    Both images need to have the same NumPy type. The result image has the same
    type as the input images and is clipped against the type's valid intensity
    range.
    """

    dtype = eqtype(I, J)
    X = convert(I, "float")
    Y = convert(J, "float")
    return convert(X - Y, dtype)


###
#%% higher level operations
###


@CV2
def dog(I, sigma1, sigma2, absdiff=False):
    """
    Difference-of-Gaussian (band-pass) filter for image `I`.

    Returns the difference image between `I` filtered by a Gaussian with sigma
    `min(sigma1, sigma2)` and `I` filtered by a Gaussian with sigma
    `max(sigma1, sigma2)`. The result has the same data type as `I`.

    If `absdiff` is `False`, the difference is signed and a difference of zero
    results in the "middle" intensity value for `I`'s data type (e.g., `127`
    for `uint8`). Otherwise, the absolute difference is used, where a
    difference of zero results in the minimum intensity value for `I`'s data
    type (e.g., `0` for `uint8`).
    """

    dtype = I.dtype
    (sigmaL, sigmaH) = tuple(dh.utils.sclip(value, lower=0.001, upper=None) for value in dh.utils.minmax(sigma1, sigma2))
    L = convert(cv2.GaussianBlur(I, None, sigmaL), "float")
    H = convert(cv2.GaussianBlur(I, None, sigmaH), "float")

    if absdiff:
        D = np.abs(L - H)
    else:
        D = (L - H) * 0.5 + 0.5
    return convert(D, dtype)


###
#%% development
###


def pinfo(I):
    """
    Prints info about the image `I`.
    """

    counter = collections.Counter(I.flatten().tolist())
    (counterArgmax, counterMax) = counter.most_common(1)[0]
    #("mode", "{} ({}%)".format(counterArgmax, round(100.0 * counterMax / info["elements"], 2))),

    info = (
        ("shape", I.shape),
        #("elements"], np.prod(I.shape)),
        ("dtype", I.dtype),
        ("mean", np.mean(I)),
        ("std", np.std(I)),
        ("min", np.min(I)),
        ("1st quartile", np.percentile(I, 25.0)),
        ("median", np.median(I)),
        ("3rd quartile", np.percentile(I, 75.0)),
        ("max", np.max(I)),
     )

    #print("=" * 40)
    #maxKeyLength = max(len(key) for key in info.keys())
    #for key in info.keys():
    #    print(("{key:.<" + str(maxKeyLength) + "} = {value}").format(key=(key + " ")[:maxKeyLength], value=info[key]))
    dh.utils.ptable(info)
