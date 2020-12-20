"""
Image pipeline viewer.

Note: currently under heavy construction.
"""

import tkinter
import tkinter.ttk

import dh.gui.tk
import dh.image


##
## basic classes
##


class Viewer():
    def __init__(self):
        self.images = []
        self.n = None
        self.pipeline = Pipeline()
        self.pipeline.add("core.convert")
        self.pipeline.add("core.asgray")
        #self.pipeline.add("core.invert")
        #self.pipeline.add("core.normalize")
        self.pipeline.add("core.shift")
        #self.pipeline.add("core.fft")
        #self.pipeline.add("core.normalize")
        self.pipeline.add("core.log")
        #self.pipeline.add("core.gamma")
        #self.pipeline.add("core.threshold")
        #self.pipeline.add("core.rotate")

    def select(self, n):
        N = len(self.images)
        if N == 0:
            self.n = None
        else:
            self.n = n % N
        return self.n

    def first(self):
        self.select(0)

    def prev(self):
        try:
            self.select(self.n - 1)
        except TypeError:
            pass

    def next(self):
        try:
            self.select(self.n + 1)
        except TypeError:
            pass

    def last(self):
        self.select(-1)

    def add(self, I):
        self.images.append(I.copy())
        self.last()

    def clear(self):
        self.images = []
        self.first()

    def show(self):
        window = _ViewerWindow(self)
        window.run()

    def view(self, I):
        self.add(I)
        self.show()

    def selectedImage(self):
        return self.images[self.n]

    def applyPipeline(self):
        return self.pipeline(self.selectedImage())


class _ViewerWindow(dh.gui.tk.Application):
    def __init__(self, viewer):
        super(_ViewerWindow, self).__init__(
            title="Viewer",
            minSize=(250, 250),
        )
        self.viewer = viewer
        self.updateFilterFrame()
        self.updateImage()

    def initWidgets(self):
        # key bindings
        self.bind("<Escape>", lambda _: self.close())
        self.bind("<q>", lambda _: self.close())
        self.bind("<Left>", lambda _: (self.viewer.prev(), self.updateImage()))
        self.bind("<Right>", lambda _: (self.viewer.next(), self.updateImage()))

        # main frame
        self.mainFrame = tkinter.ttk.Frame(self)
        self.mainFrame.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=tkinter.YES)

        # filter frame
        self.filterFrame = tkinter.ttk.Frame(self.mainFrame)
        self.filterFrame.pack(side=tkinter.LEFT, anchor=tkinter.N, padx=2, pady=2)

        # image canvas
        self.imageCanvas = dh.gui.tk.ImageCanvas(self.mainFrame)
        self.imageCanvas.pack(side=tkinter.LEFT, anchor=tkinter.N, fill=tkinter.BOTH, expand=tkinter.YES)

        # status bar
        self.statusBar = dh.gui.tk.StatusBar(self)
        self.statusBar.pack(side=tkinter.BOTTOM, fill=tkinter.X, expand=tkinter.NO)

    def updateFilterFrame(self):
        for node in self.viewer.pipeline.nodes:
            node.gui(parent=self.filterFrame, onChangeCallback=self.updateImage).pack(fill="x", padx=1, pady=1, expand=True)

    def updateImage(self, *args, **kwargs):
        with dh.utils.Timer() as t:
            I = self.viewer.applyPipeline()
        self.imageCanvas.setImage(I)
        self.updateStatusBar("{shape}, {dtype}, {time}ms".format(
            shape=I.shape,
            dtype=I.dtype,
            time=dh.utils.around(t() * 1000.0),
        ))

    def updateStatusBar(self, text):
        self.statusBar.setText(text)


##
## pipeline framework
##


class Pipeline():
    def __init__(self):
        # nodes
        self.nodes = []
        self.add("core.source")

    def __call__(self, I):
        J = I.copy()
        for node in self.nodes:
            J = node(J)
        return J

    def add(self, node, position=None):
        """
        Inserts processing before the `position`-th slot of the pipeline.
        """

        if position is None:
            position = len(self.nodes)

        if isinstance(node, str):
            uid = node
            node = Node.instances[uid]
        self.nodes.insert(position, node)

    def remove(self, position):
        del self.nodes[position]

    def save(self, filename):
        raise NotImplementedError()

    def load(self, filename):
        raise NotImplementedError()


class Node():
    """
    Class for a processing pipeline element (node), which automatically
    registers its instances.
    """

    # keeps references to all instances of this class
    instances = {}

    def __init__(self, uid, description=None, tags=None, f=None, parameters=(), cache=False):
        # register this instance
        if uid not in type(self).instances:
            type(self).instances[uid] = self
        else:
            raise ValueError("Node with uid '{uid}' is already registered".format(uid=uid))

        # other properties
        self.uid = uid
        self.description = description
        self.tags = tags
        self.f = f
        self.parameters = list(parameters)

        # cache
        self.useCache = cache
        self.cache = {}

    def __call__(self, *args, **kwargs):
        kwargs.update(self.parameterValues())
        if self.useCache:
            key = dh.utils.ohash((args, kwargs), "hex", 64)
            if key not in self.cache:
                self.cache[key] = self.f(*args, **kwargs)
            return self.cache[key]
        else:
            return self.f(*args, **kwargs)

    def parameterValues(self):
        return {parameter.name: parameter() for parameter in self.parameters}

    def gui(self, parent, onChangeCallback):
        """
        Constructs and returns a GUI frame for this filter.
        """

        # master frame
        frame = tkinter.ttk.Frame(parent, relief="raised")

        # usable part of the frame
        innerFrame = tkinter.ttk.Frame(frame)
        innerFrame.pack(fill="x", expand=True, padx=6, pady=3)

        # header line
        header = tkinter.ttk.Frame(innerFrame)
        header.pack(side = tkinter.TOP, fill = "x", expand = True)
        tkinter.ttk.Label(header, text=self.uid, font="Sans 10 bold", anchor = tkinter.W, justify = tkinter.LEFT).pack(side = tkinter.LEFT, fill = "x", expand = True)

        # description line
        if self.description is not None:
            details = tkinter.ttk.Frame(innerFrame)
            details.pack(side = tkinter.TOP, fill = "x", expand = True)
            tkinter.ttk.Label(details, text=self.description, font="Sans 8 italic", anchor = tkinter.W, justify = tkinter.LEFT).pack(side = tkinter.LEFT, fill = "x", expand = True)

        # parameter frame
        parameterFrame = tkinter.ttk.Frame(innerFrame)
        parameterFrame.pack(side = tkinter.TOP, fill = "x", expand = True)
        for (row, parameter) in enumerate(self.parameters):
            (labelFrame, valueFrame) = parameter.gui(parent=parameterFrame, onChangeCallback=onChangeCallback)
            labelFrame.grid(row = row, column = 0, padx = 0, sticky = tkinter.W)
            valueFrame.grid(row = row, column = 1, padx = 10, sticky = tkinter.W)

            #tkinter.ttk.Scale(parameterFrame, from_=0, to=100).grid(row = n, column = 1)

        return frame


class SwitchableNode(Node):
    """
    Processing node which automatically has one bool parameter to enable or
    disable the processing.
    """

    def __init__(self, *args, **kwargs):
        # parent initialization
        super().__init__(*args, **kwargs)

        # add "enabled" parameter
        self.parameters = [
            BoolNodeParameter(
                name="enabled",
                default=True,
            )
        ] + self.parameters

        # wrap function
        self.g = self.f
        def f(I, enabled, **kwargs):
            if enabled:
                return self.g(I=I, **kwargs)
            else:
                return I
        self.f = f


class NodeParameter():
    def __init__(self, name, label=None):
        self.name = name
        if label is not None:
            self.label = label
        else:
            self.label = name

    def guiLabelFrame(self, parent):
        return tkinter.ttk.Label(parent, text=self.label, font="Sans 8", anchor = tkinter.W, justify = tkinter.LEFT)

    def guiValueFrame(self, parent, onChangeCallback):
        raise NotImplementedError("Use a subclass of 'NodeParameter'")

    def gui(self, parent, onChangeCallback):
        return (
            self.guiLabelFrame(parent=parent),
            self.guiValueFrame(parent=parent, onChangeCallback=onChangeCallback),
        )

    def __call__(self):
        raise NotImplementedError("Use a subclass of 'NodeParameter'")


class BoolNodeParameter(NodeParameter):
    def __init__(self, name, label=None, default=True):
        super().__init__(name=name, label=label)
        self.default = default
        self.variable = None

    def guiValueFrame(self, parent, onChangeCallback):
        self.variable = tkinter.IntVar()
        self.variable.set(self.default)
        return tkinter.ttk.Checkbutton(parent, text="", variable=self.variable, command=onChangeCallback, takefocus=tkinter.NO)

    def __call__(self):
        if self.variable is not None:
            return bool(self.variable.get())
        else:
            return None


class RangeNodeParameter(NodeParameter):
    def __init__(self, name, label=None, start=0.0, end=1.0, step=0.01, default=0.0):
        super().__init__(name=name, label=label)
        self.start = start
        self.end = end
        self.step = step
        self.default = default
        self.slider = None

    def guiValueFrame(self, parent, onChangeCallback):
        self.slider = tkinter.ttk.Scale(parent, from_=self.start, to=self.end, command=onChangeCallback)
        self.slider.set(self.default)
        return self.slider

    def __call__(self):
        if self.slider is not None:
            return self.slider.get()
        else:
            return None


class SelectionNodeParameter(NodeParameter):
    """
    The parameter value can be chosen from a list of possible values.
    """

    def __init__(self, name, label=None, values=(), default=None):
        super().__init__(name=name, label=label)
        self.labels = (str(value) for value in values)
        self.values = {str(value): value for value in values}
        if (default is not None) and (default in values):
            self.default = str(default)
        elif len(values) > 0:
            self.default = str(values[0])
        else:
            self.default = None
        self.variable = None

    def guiValueFrame(self, parent, onChangeCallback):
        # create variable and set default value
        self.variable = tkinter.StringVar()
        if self.default is not None:
            self.variable.set(self.default)

        # create dropdown menu
        select = tkinter.OptionMenu(parent, self.variable, *self.labels, command=onChangeCallback)
        select.config(width = 10)

        return select

    def __call__(self):
        if self.variable is not None:
            return self.values[self.variable.get()]
        else:
            return None


##
## pipeline processing nodes
##


Node(
    uid="core.source",
    description="Original image",
    f=dh.image.identity,
)

SwitchableNode(
    uid="core.convert",
    f=dh.image.convert,
    parameters=[
        SelectionNodeParameter(
            name="dtype",
            values=("uint8", "uint16", "float"),
            default="uint8",
        ),
    ],
)

SwitchableNode(
    uid="core.asgray",
    f=dh.image.asgray,
)

SwitchableNode(
    uid="core.invert",
    f=dh.image.invert,
)

Node(
    uid="core.normalize",
    f=dh.image.normalize,
    parameters=[
        SelectionNodeParameter(
            name="mode",
            values=("none", "minmax", "percentile"),
            default="percentile",
        ),
        RangeNodeParameter(
            name="q",
            start=0.0,
            end=50.0,
            step=0.1,
            default=2.0,
        ),
    ],
)

SwitchableNode(
    uid="core.log",
    f=dh.image.log,
)

SwitchableNode(
    uid="core.gamma",
    description="Power-law transformation",
    f=dh.image.gamma,
    parameters=[
        RangeNodeParameter(
            name="gamma",
            start=1.0,
            end=10.0,
            step=0.01,
            default=1.0,
        ),
        BoolNodeParameter(
            name="inverse",
            default=False,
        ),
    ],
    cache=True,
)

SwitchableNode(
    uid="core.threshold",
    description="Global threshold",
    f=lambda I, theta: dh.image.threshold(I=I, theta=theta, relative=True),
    parameters=[
        RangeNodeParameter(
            name="theta",
            start=0.0,
            end=1.0,
            step=0.01,
            default=0.5,
        ),
    ],
)

SwitchableNode(
    uid="core.shift",
    f=dh.image.shift,
    parameters=[
        RangeNodeParameter(
            name="dx",
            start=0.0,
            end=1.0,
            step=0.01,
            default=0.0,
        ),
        RangeNodeParameter(
            name="dy",
            start=0.0,
            end=1.0,
            step=0.01,
            default=0.0,
        ),
    ],
)

SwitchableNode(
    uid="core.rotate",
    f=dh.image.rotate,
    parameters=[
        SelectionNodeParameter(
            name="degree",
            values=(0, 90, 180, 270),
            default=90,
        )
    ],
)

#SwitchableNode(
#    uid="core.fft",
#    f=dh.image.fft,
#)
