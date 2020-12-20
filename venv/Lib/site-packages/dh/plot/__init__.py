"""
Tools for data visualization.
"""

import abc
import collections
import json
import textwrap
import warnings

import dh.utils
import dh.data

try:
    from matplotlib import pyplot as plt
    PLT_ERROR = None
except ImportError as e:
    plt = None
    PLT_ERROR = e


###
#%%
###


def scatter(xs, ys, labels=None, colormap="plot", uniqueLabels=None):
    """
    Draws a scatter plot.

    The x coordinates, y coordinates and labels of the points are specified via
    `xs`, `ys`, `labels`. If no labels are given, the points will not be
    colored. Otherwise, points will be colored according to their label. The
    argument `uniqueLabels` can be used to specify the ordering in which the
    labels should appear in the legend.
    """

    if plt is None:
        raise PLT_ERROR

    if labels is None:
        plt.scatter(xs, ys)
    else:
        if uniqueLabels is None:
            uniqueLabels = tuple(dh.utils.unique(labels))

        # split points based on the labels
        xss = collections.defaultdict(list)
        yss = collections.defaultdict(list)
        for (x, y, label) in zip(xs, ys, labels):
            try:
                nUniqueLabel = uniqueLabels.index(label)
            except ValueError:
                warnings.warn("Label '{}' is not in the list of provided unique labels - skipping data point".format())
            else:
                xss[nUniqueLabel].append(x)
                yss[nUniqueLabel].append(y)

        c = dh.data.colormap(colormap)
        plots = []
        for nUniqueLabel in xss.keys():
            try:
                color = c[nUniqueLabel]
            except KeyError:
                color = (127, 127, 127)
                warnings.warn("Colormap '{}' defines no color for value '{}'".format(colormap, nUniqueLabel))
            color = tuple(channel / 255.0 for channel in color)

            plot = plt.scatter(xss[nUniqueLabel], yss[nUniqueLabel], color=color)
            plots.append(plot)

        plt.legend(plots, uniqueLabels, loc="best", scatterpoints=1)
        plt.show()


###
#%% Google charts wrapper
###


class GoogleCharts():
    """
    Wrapper for Google charts (https://developers.google.com/chart/).

    This class creates an empty "container" to which multiple charts (instances
    of class `GoogleChart` can be added (see :func:`GoogleCharts.append()`).

    `api` can be used to specify the version of the Google chart API. It must
    be a string and can either contain a number (e.g., `"45"`) or the value
    `"current"`).

    .. todo:: Allow user to specify the width/height of DIV elements.
    """

    def __init__(self, api="current"):
        self._api = api
        self.charts = []

    @property
    def api(self):
        """
        Property which gets the API version of this Google chart container.
        """
        return self._api

    def append(self, chart):
        """
        Append chart to this Google charts object.
        """

        if not isinstance(chart, GoogleChart):
            raise TypeError("Argument 'chart' must be of type 'GoogleChart' (but '{}' was provided)".format(type(chart)))
        if chart.uid is None:
            chart.uid = "{:>04d}".format(len(self.charts))
        self.charts.append(chart)

    def renderJs(self):
        """
        Returns string of the JavaScript code which draws all charts of this
        container.
        """

        template = """
            <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
            <script type="text/javascript">
                //google.charts.load('current', {{'packages':['corechart']}});
                google.charts.load({api}, {{'packages':['corechart']}});
                google.charts.setOnLoadCallback(drawAllCharts);

                {functions}

                function drawAllCharts() {{
                    {functionCalls}
                }}
            </script>
        """

        return textwrap.dedent(template).format(
            api=json.dumps(self.api),
            functions="\n".join(chart.renderFunctionJs() for chart in self.charts),
            functionCalls="\n".join("{}();".format(chart.functionName()) for chart in self.charts),
        )

    def renderDivs(self):
        """
        Returns string of the HTML `div` elements needed to draw the charts of
        this container.
        """
        return "\n".join("<div id=\"{}\" style=\"margin:50px auto; width: 800px; height: 800px;\"></div>".format(chart.divName()) for chart in self.charts)

    def renderHtml(self):
        """
        Return string containing the entire HTML code needed to render all
        charts that were added to this container.
        """

        template = """
            <html>
                <head>
                    {js}
                    <style>
                        body {{
                            background-color: #EEE;
                            text-align: center;
                        }}
                        div.chart {{
                            margin: 50px auto;
                        }}
                    </style>
                </head>
                <body>
                    {divs}
                </body>
            </html>
        """

        return textwrap.dedent(template).format(
            js=self.renderJs(),
            divs=self.renderDivs(),
        )

    def save(self, filename):
        """
        Render HTML code and save it to file `filename`.

        Directories are created as necessary.
        """

        dh.utils.mkpdir(filename)
        with open(filename, "w") as f:
            f.write(self.renderHtml())


class GoogleChart(abc.ABC):
    """
    Base class for an individual Google chart which can be added to a
    `GoogleCharts` container.

    `uid` must be a unique string which is used to reference the plot in the
    generated JavaScript and HTML code. If it is `None`, the Google chart
    container chooses a unique value.

    `options` can be `None` or a dictionary containing key/value pairs as
    documented in https://developers.google.com/chart/interactive/docs/basic_customizing_chart#specify-options.
    If it is `None`, an empty dictionary is created.
    """

    _optionsDefault = {
        "chartArea": {"width": "70%", "height": "70%"},
    }

    def __init__(self, uid=None, options=None):
        self._uid = uid
        if options is None:
            options = {}
        self._options = dh.utils.rupdate(self._optionsDefault, options)
        self._header = []
        self._data = []

    @property
    def uid(self):
        """
        Property which can be used to get and set the UID of this chart.
        """
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value

    ##
    ##
    ##

    @property
    def header(self):
        """
        Property which can be used to get and set the header of the data
        table of this chart.
        """
        return self._header

    @header.setter
    def header(self, value):
        if value is not None:
            self._header = [value]
        else:
            self._header= []

    @property
    def data(self):
        """
        Property which gets the data table of this chart.
        """
        return self._data

    ##
    ## options
    ##

    @property
    def options(self):
        """
        Property which gets the option dictionary.
        """
        return self._options

    @property
    def title(self):
        """
        Property which can be used to get and set the title of this chart.
        """
        try:
            return self.options["title"]
        except KeyError:
            return None

    @title.setter
    def title(self, value):
        self.options["title"] = str(value)

    ##
    ## rendering
    ##

    @staticmethod
    @abc.abstractmethod
    def _chartClass():
        pass

    @staticmethod
    def renderObject(obj):
        """
        Render Python object `obj` (e.g., a list or a dictionary) as
        JavaScript object.
        """
        return json.dumps(obj, indent=4, sort_keys=True)

    def functionName(self):
        """
        Return this plot's JavaScript function name.
        """
        return "chart_{uid}_draw".format(uid=self.uid)

    def divName(self):
        """
        Return this plot's HTML div-element name.
        """
        return "chart_{uid}_div".format(uid=self.uid)

    def renderFunctionJs(self):
        """
        Return the JavaScript function needed to draw this plot.
        """
        template = """
            function {functionName}() {{
                var data = google.visualization.arrayToDataTable({data});

                var options = {options};

                var chart = new {chartClass}(document.getElementById('{divName}'));
                chart.draw(data, options);
            }}
        """
        return textwrap.dedent(template).format(
            functionName=self.functionName(),
            data=self.renderObject(self.header + self.data),
            options=self.renderObject(self.options),
            chartClass=self._chartClass(),
            divName=self.divName(),
        )


class GoogleColumnChart(GoogleChart):
    """
    Column (bar) chart which can be added to a `GoogleCharts` container.

    `xs` must be a iterable specifying the x values of the chart (which can be
    numerics or strings). `yss` must be either an iterable of the same length
    as `xs` or a dictionary of iterables, each of the same length as `xs`. In
    the first case, the chart will have one bar per value in `xs`. In the
    second case, there will be as many bars per value in `xs` as there are
    keys in `yss`.

    .. note:: Use `collections.OrderedDict` to order the bars.

    >>> c = GoogleColumnChart(xs=["a", "b", "c", "d"], yss=[1, 2, 3, 4])

    >>> c = GoogleColumnChart(xs=[1, 2, 3, 4], yss={"bar1": [1, 2, 3, 4], "bar2": [2, 3, 2, 1]})
    """

    def __init__(self, xs, yss, **kwargs):
        super().__init__(**kwargs)

        # header
        labeled = isinstance(yss, dict)
        if labeled:
            ulabels = tuple(dh.utils.unique(yss.keys()))
            self.header = ("x",) + ulabels
        else:
            self.header = ("x", "y")

        # data
        rowCount = len(xs)
        for nRow in range(rowCount):
            if labeled:
                row = [xs[nRow]] + [yss[label][nRow] for label in ulabels]
            else:
                row = (xs[nRow], yss[nRow])
            self._data.append(row)

    @staticmethod
    def _chartClass():
        return "google.visualization.ColumnChart"


class GoogleScatterChart(GoogleChart):
    """
    Scatter chart which can be added to a `GoogleCharts` container.

    `xs` and `ys` must be iterables of equal length specifying the x and y
    coordinates of the points to be plotted. If `labels` is `None`, all
    points have the same color. Otherwise, to visually group points, `labels`
    must be an iterable of strings with the same length as `xs` and `ys`, which
    indicates which label each point to be plotted should have.

    >>> c = GoogleScatterChart(xs=[3, 5, 3, 5, 4], ys=[3, 2, 1, 5, 1])

    >>> c = GoogleScatterChart(xs=[3, 5, 3, 5, 4], ys=[3, 2, 1, 5, 1], labels=["a", "b", "a", "b", "a"])
    """

    def __init__(self, xs, ys, labels=None, **kwargs):
        super().__init__(**kwargs)

        # header
        labeled = (labels is not None)
        if labeled:
            ulabels = tuple(dh.utils.unique(labels))
            labelCount = len(ulabels)
            self.header = ("x",) + ulabels
        else:
            self.header = ("x", "y")

        # data
        rowCount = len(xs)
        for nRow in range(rowCount):
            if labeled:
                row = [None] * (labelCount + 1)
                row[0] = xs[nRow]
                row[ulabels.index(labels[nRow]) + 1] = ys[nRow]
            else:
                row = (xs[nRow], ys[nRow])
            self._data.append(row)

    @staticmethod
    def _chartClass():
        return "google.visualization.ScatterChart"


class GoogleLineChart(GoogleChart):
    """
    Line chart which can be added to a `GoogleCharts` container.

    `xs` must be a iterable specifying the x values of the chart. `yss` must be
    either an iterable or a dictionary of iterables. If `yss` is an iterable,
    the chart will have one line with y values according to `yss`. If `yss` is
    a dictionary of iterables, the chart will have multiple lines, where the
    y values are given by each iterable of the dictionary. The dictionary keys
    will then serve as labels.

    .. note:: Use `collections.OrderedDict` for `yss` to order the labels.

    >>> c = GoogleLineChart(xs=[1, 2, 3, 4, 5], yss=[1, 4, 9, 16, 25])

    >>> c = GoogleLineChart(xs=[1, 2, 3, 4, 5], yss={"x**2": [1, 4, 9, 16, 25], "x**3": [1, 8, 27, 64, 125]})
    """

    def __init__(self, xs, yss, **kwargs):
        super().__init__(**kwargs)

        # header
        labeled = isinstance(yss, dict)
        if labeled:
            ulabels = tuple(dh.utils.unique(yss.keys()))
            self.header = ("x",) + ulabels
        else:
            self.header = ("x", "y")

        # data
        rowCount = len(xs)
        for nRow in range(rowCount):
            if labeled:
                row = [xs[nRow]] + [yss[label][nRow] for label in ulabels]
            else:
                row = (xs[nRow], yss[nRow])
            self._data.append(row)

    @staticmethod
    def _chartClass():
        return "google.visualization.LineChart"
