"""
Tools for logging.
"""

import abc
import datetime
import os.path
import pprint

import dh.utils
import dh.thirdparty.colorama


###
#%% colorama
###


# foreground colors
FG_RESET   = dh.thirdparty.colorama.Fore.RESET
FG_BLACK   = dh.thirdparty.colorama.Fore.BLACK
FG_RED     = dh.thirdparty.colorama.Fore.RED
FG_GREEN   = dh.thirdparty.colorama.Fore.GREEN
FG_YELLOW  = dh.thirdparty.colorama.Fore.YELLOW
FG_BLUE    = dh.thirdparty.colorama.Fore.BLUE
FG_MAGENTA = dh.thirdparty.colorama.Fore.MAGENTA
FG_CYAN    = dh.thirdparty.colorama.Fore.CYAN
FG_WHITE   = dh.thirdparty.colorama.Fore.WHITE

# background colors
BG_RESET   = dh.thirdparty.colorama.Back.RESET
BG_BLACK   = dh.thirdparty.colorama.Back.BLACK
BG_RED     = dh.thirdparty.colorama.Back.RED
BG_GREEN   = dh.thirdparty.colorama.Back.GREEN
BG_YELLOW  = dh.thirdparty.colorama.Back.YELLOW
BG_BLUE    = dh.thirdparty.colorama.Back.BLUE
BG_MAGENTA = dh.thirdparty.colorama.Back.MAGENTA
BG_CYAN    = dh.thirdparty.colorama.Back.CYAN
BG_WHITE   = dh.thirdparty.colorama.Back.WHITE


def cinit():
    """
    Initialize colorama.
    """
    dh.thirdparty.colorama.init(autoreset=True)


def cdeinit():
    """
    De-initialize colorama.
    """
    dh.thirdparty.colorama.deinit()


###
#%% logger
###


class LoggerFormatter(abc.ABC):
    """
    Base class for logger formatters.

    A simple way to create a new formatter is to implement the method
    `getPreAndPostfixes()`. For absolute freedom, implement the `apply()`
    method.
    """

    def getLevelColor(self, level):
        """
        Return a color for the given log level.
        """
        if level >= Logger.LEVEL_CRITICAL:
            return FG_WHITE + BG_RED
        elif level >= Logger.LEVEL_ERROR:
            return FG_RED + BG_RESET
        elif level >= Logger.LEVEL_WARNING:
            return FG_YELLOW + BG_RESET
        elif level >= Logger.LEVEL_SUCCESS:
            return FG_GREEN + BG_RESET
        elif level >= Logger.LEVEL_INFO:
            return FG_RESET + BG_RESET
        else:
            return FG_CYAN + BG_RESET

    def getLevelName(self, level):
        """
        Return a name for the given log level.
        """
        if level >= Logger.LEVEL_CRITICAL:
            return "CRITICAL"
        elif level >= Logger.LEVEL_ERROR:
            return "ERROR"
        elif level >= Logger.LEVEL_WARNING:
            return "WARNING"
        elif level >= Logger.LEVEL_SUCCESS:
            return "SUCCESS"
        elif level >= Logger.LEVEL_INFO:
            return "INFO"
        else:
            return "DEBUG"

    @abc.abstractmethod
    def getPreAndPostfixes(self, level, **kwargs):
        pass

    def apply(self, text, level, **kwargs):
        """
        Takes the log message `text`, the log level `level`, and returns the
        formatted (final) output string.
        """
        (pre1, pre2, post1, post2) = self.getPreAndPostfixes(level=level, **kwargs)
        outLines = []
        for (nLine, line) in enumerate(text.splitlines()):
            if nLine == 0:
                s = pre1 + line + post1
            else:
                s = pre2 + line + post2
            outLines.append(s)
        return "\n".join(outLines)


class PlainLoggerFormatter(LoggerFormatter):
    """
    This formatter returns the log text as-is.
    """
    def getPreAndPostfixes(self, level, **kwargs):
        return ("",) * 4


class MinimalLoggerFormatter(LoggerFormatter):
    """
    This formatter only colorizes the log messages according to their level and
    adds an indent for multi-line log messages.
    """
    def getPreAndPostfixes(self, level, **kwargs):
        color = self.getLevelColor(level)
        pre1 = color
        pre2 = color + "  "
        post1 = post2 = FG_RESET + BG_RESET
        return (pre1, pre2, post1, post2)


class BulletLoggerFormatter(LoggerFormatter):
    """
    This formatter creates colorized, bulleted log messages.
    """
    def getPreAndPostfixes(self, level, **kwargs):
        color = self.getLevelColor(level)
        pre1 = color + "* "
        pre2 = color + "  "
        post1 = post2 = FG_RESET + BG_RESET
        return (pre1, pre2, post1, post2)


class ShortLoggerFormatter(LoggerFormatter):
    """
    This formatter creates an output containing the log message level.
    """
    def getLevelName(self, level):
        name = super().getLevelName(level)
        if name == "DEBUG":
            name = "DBUG"
        elif name == "SUCCESS":
            name = " OK "
        elif name == "ERROR":
            name = "FAIL"
        return name[:4]

    def getPreAndPostfixes(self, level, **kwargs):
        # color and level name
        color = self.getLevelColor(level)
        name = self.getLevelName(level)
        pre1 = FG_RESET + "[" + color + name + FG_RESET + BG_RESET + "]  "
        pre2 = " " * 8
        post1 = FG_RESET + BG_RESET
        post2 = FG_RESET + BG_RESET
        return (pre1, pre2, post1, post2)


class LongLoggerFormatter(LoggerFormatter):
    """
    This formatter creates a long output including the time of the log message.
    """
    def getLevelName(self, level):
        name = super().getLevelName(level)
        return name[0]

    def getPreAndPostfixes(self, level, timestamp, **kwargs):
        # color and level name
        color = self.getLevelColor(level)
        name = self.getLevelName(level)
        dtstr = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
        pre1 = color + "[" + dtstr + "]" + "  " + name + "  "
        pre2 = color + " " * (len(dtstr) + len(name) + 6)
        post1 = FG_RESET + BG_RESET
        post2 = FG_RESET + BG_RESET
        return (pre1, pre2, post1, post2)


class PendingLoggerMessage():
    def __init__(self, logger, text):
        self.logger = logger
        self.text = text

    def log(self, logFunc, extraText=""):
        text = self.text
        if extraText is not None:
            text += "\n" + extraText
        logFunc(text)

    def ok(self, *args, **kwargs):
        self.log(self.logger.ok, *args, **kwargs)

    def failed(self, *args, **kwargs):
        self.log(self.logger.failed, *args, **kwargs)


class Logger():
    # levels
    LEVEL_DEBUG    = 10
    LEVEL_INFO     = 20
    LEVEL_SUCCESS  = 25
    LEVEL_WARNING  = 30
    LEVEL_ERROR    = 40
    LEVEL_CRITICAL = 50

    def __init__(self, formatter="long", filename=None, minLevel=None, color=True):
        """
        Creates a logger instance which can be used to create log messages
        which can be printed on the screen and saved to file.

        The argument `formatter` can be a scalar (either string or an instance
        of `LoggerFormatter`) in which case it is used for printing to screen
        and saving to file. Alternatively, it can be a 2-tuple specifying
        different formatters for printing and saving.

        If `filename` is `None`, no log messages are written to file. If it is
        a directory name, a file with a timestamped name is created in that
        directory and used for saving log messages. If is is a regular
        filename, that file is used for saving log messages. Log messages are
        always appended to the log file.

        `minLevel` specifies the minimum level of a log message in order to be
        shown. It can be either a scalar (one of `Logger.LEVEL_*`) in which
        case it is used for both printing on screen and saving to file.
        Otherwise, it can be a 2-tuple allowing different settings for printing
        and saving.

        If `color` is `False`, colorized outputs are disabled when printing log
        messages on the screen.
        """

        # set print and save formatter and min level
        self.setFormatter(formatter)
        self.setMinLevel(minLevel)
        self.color = color
        if color:
            cinit()

        # filename for saving
        if filename is None:
            self.saveFilename = None
        elif isinstance(filename, str):
            if os.path.isdir(filename):
                self.saveFilename = "{}.log".format(dh.utils.dtstr(compact=True))
            else:
                self.saveFilename = filename

        #self.colored = colored
        #self.inspect = inspect
        #if self.colored:
        #    cinit()

    @staticmethod
    def getFormatterInstance(formatter):
        if isinstance(formatter, str):
            formatter = formatter.lower()
            if formatter == "plain":
                return PlainLoggerFormatter()
            elif formatter == "minimal":
                return MinimalLoggerFormatter()
            elif formatter == "bullet":
                return BulletLoggerFormatter()
            elif formatter == "short":
                return ShortLoggerFormatter()
            elif formatter == "long":
                return LongLoggerFormatter()
            else:
                raise ValueError("Invalid formatter '{}'".format(formatter))
        elif isinstance(formatter, LoggerFormatter):
            return formatter
        else:
            raise ValueError("Invalid formatter '{}'".format(formatter))

    def setFormatter(self, formatter):
        (self.printFormatter, self.saveFormatter) = [self.getFormatterInstance(f) for f in dh.utils.dntup(formatter, 2)]

    def setMinLevel(self, level):
        (self.printMinLevel, self.saveMinLevel) = dh.utils.dntup(level, 2)

    def log(self, text, level):
        timestamp = datetime.datetime.now()

        if (self.printMinLevel is None) or (level >= self.printMinLevel):
            s = self.printFormatter.apply(text=text, level=level, timestamp=timestamp)
            if not self.color:
                s = dh.utils.uncolorize(s)
            print(s)

        # write log message to file
        if (self.saveFilename is not None) and ((self.saveMinLevel is None) or (level >= self.saveMinLevel)):
            with open(self.saveFilename, "a") as f:
                s = self.saveFormatter.apply(text=text, level=level, timestamp=timestamp)
                f.write(dh.utils.uncolorize(s) + "\n")

    ###
    #%% basic log types
    ###

    def debug(self, text):
        self.log(text=text, level=Logger.LEVEL_DEBUG)

    def info(self, text):
        self.log(text=text, level=Logger.LEVEL_INFO)

    def success(self, text):
        self.log(text=text, level=Logger.LEVEL_SUCCESS)

    def warning(self, text):
        self.log(text=text, level=Logger.LEVEL_WARNING)

    def error(self, text):
        self.log(text=text, level=Logger.LEVEL_ERROR)

    def critical(self, text):
        self.log(text=text, level=Logger.LEVEL_CRITICAL)

    ###
    #%% aliases
    ###

    def ok(self, text):
        self.success(text=text)

    def fail(self, text):
        self.error(text=text)

    def failed(self, text):
        self.error(text=text)

    ###
    #%% extended log functionality
    ###

    def pending(self, text):
        """
        Returns a pending log message (see class `PendingLoggerMessage`), i.e.
        a log message with unknown log level. The message is logged once a
        method such as `ok()` or `fail()` is called.

        Useful if the the log level is not known when the log text is specified
        (e.g., when an operation can succeed or fail).

        Example:
            msg = logger.pending("Starting service...")
            if ok:
                msg.ok()
            else:
                msg.fail("Error at step 7")
        """
        return PendingLoggerMessage(logger=self, text=text)

    def pprint(self, x, name=None, **kwargs):
        """
        Creates a debug log message of the pretty printed object `x`. If `name`
        is given, it is added at the beginning of the debug output.
        """
        text = pprint.pformat(x, **kwargs)
        if name is not None:
            text = str(name) + " = " + text
        self.debug(text)
