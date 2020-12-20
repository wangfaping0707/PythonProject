"""
GUI-related functions.
"""


def screenres():
    """
    Return the resolution (width x height) of the screen in pixels.

    .. seealso:: http://stackoverflow.com/a/3949983
    """

    try:
        import tkinter as tk
    except ImportError:
        return (None, None)

    root = tk.Tk()
    (W, H) = (root.winfo_screenwidth(), root.winfo_screenheight())
    root.destroy()
    return (W, H)
