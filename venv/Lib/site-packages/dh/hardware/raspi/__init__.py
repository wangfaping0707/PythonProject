import io
import time

import dh.utils
import dh.image
import dh.network


class CameraServer(dh.network.SocketServer):
    # command bytes
    COMMAND_PING    = 0x0
    COMMAND_GET     = 0x1
    COMMAND_SET     = 0x2
    COMMAND_CAPTURE = 0x3

    # response bytes corresponding to the commands are identical to the command byte - below are therefore just responses which have no command counterpart
    RESPONSE_ERROR  = 0xFF

    # attributes which can be get/set
    GET_SET_ATTRIBUTES = [
        "analog_gain",
        "awb_gains",
        "awb_mode",
        "brightness",
        "contrast",
        "digital_gain",
        "drc_strength",
        "exposure_compensation",
        "exposure_mode",
        "exposure_speed",
        "flash_mode",
        "framerate",
        #"framerate_delta",
        #framerate_range
        "hflip",
        "image_denoise",
        "image_effect",
        "image_effect_params",
        "iso",
        #led
        "meter_mode",
        #overlays
        #preview
        #preview_alpha
        #preview_fullscreen
        #preview_layer
        #preview_window
        #recording
        "resolution",
        #"revision",
        "rotation",
        "saturation",
        "sensor_mode",
        "sharpness",
        "shutter_speed",
        "still_stats",
        #"timestamp",
        "vflip",
        "video_denoise",
        "video_stabilization",
        "zoom",
    ]

    def __init__(self, camera, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._camera = camera

    def get(self, keys):
        result = {}
        for key in keys:
            try:
                if key not in CameraServer.GET_SET_ATTRIBUTES:
                    raise AttributeError("Invalid attribute '{}'".format(key))
                value = getattr(self._camera, key)
                result[key] = value
            except Exception as e:
                result[key] = "{}: {}".format(type(e).__name__, str(e))
        return result

    def set(self, values):
        result = {}
        for (key, value) in values.items():
            try:
                if key not in CameraServer.GET_SET_ATTRIBUTES:
                    raise AttributeError("Invalid attribute '{}'".format(key))
                setattr(self._camera, key, value)
            except Exception as e:
                result[key] = "{}: {}".format(type(e).__name__, str(e))
            else:
                result[key] = "OK"
        return result

    def communicate(self, socket):
        # receive command byte
        command = socket.mrecv(dh.network.ByteSocketMessageType())

        # check for correct command byte
        if (len(command) != 1) or (int(command[0]) not in (CameraServer.COMMAND_PING, CameraServer.COMMAND_GET, CameraServer.COMMAND_SET, CameraServer.COMMAND_CAPTURE)):
            # if command is invalid, send ERROR response
            socket.msend(dh.network.ByteSocketMessageType(), bytes([CameraServer.RESPONSE_ERROR]))
            return

        # send command byte back as response
        socket.msend(dh.network.ByteSocketMessageType(), command)

        # handle PING command
        command = int(command[0])
        if command == CameraServer.COMMAND_PING:
            return

        # handle GET ommand
        elif command == CameraServer.COMMAND_GET:
            keys = socket.mrecv(dh.network.ExtendedJsonSocketMessageType())
            result = self.get(keys)
            socket.msend(dh.network.ExtendedJsonSocketMessageType(), result)
            return

        # handle SET command
        elif command == CameraServer.COMMAND_SET:
            values = socket.mrecv(dh.network.ExtendedJsonSocketMessageType())
            result = self.set(values)
            socket.msend(dh.network.ExtendedJsonSocketMessageType(), result)
            return

        # handle CAPTURE command
        elif command == CameraServer.COMMAND_CAPTURE:
            # receive parameters and overwrite defaults
            params = socket.mrecv(dh.network.ExtendedJsonSocketMessageType())
            captureKwargs = {
                "use_video_port": True,
                "format": "jpeg",
                "quality": 80,
                "thumbnail": None,
                "bayer": False,
            }
            for (key, value) in params.items():
                captureKwargs[key] = value
            if "output" in captureKwargs:
                del captureKwargs["output"]

            # capture image to byte array
            b = io.BytesIO()
            self._camera.capture(output=b, **captureKwargs)

            # send image
            socket.msend(dh.network.ByteSocketMessageType(), b.getvalue())
            return


class CameraClient(dh.network.SocketClient):
    def communicate(self, socket, command, **kwargs):
        ##
        ## checks before starting the communication with the server
        ##

        # check command byte
        if command not in (CameraServer.COMMAND_PING, CameraServer.COMMAND_GET, CameraServer.COMMAND_SET, CameraServer.COMMAND_CAPTURE):
            raise ValueError("Invalid command '{}'".format(command))

        # check kwargs
        if command == CameraServer.COMMAND_SET:
            assert(isinstance(kwargs["values"], dict))
        elif command == CameraServer.COMMAND_GET:
            assert(isinstance(kwargs["keys"], (tuple, list)))
        elif command == CameraServer.COMMAND_CAPTURE:
            assert(isinstance(kwargs["params"], dict))

        ##
        ## communication with server
        ##

        # send command byte and get response
        socket.msend(dh.network.ByteSocketMessageType(), bytes([command]))
        response = socket.mrecv(dh.network.ByteSocketMessageType())

        # check for correct response byte
        if (len(response) != 1) or (int(response[0]) != command):
            raise RuntimeError("Invalid response from server (got '{}', expected '{}')".format(response, bytes([command])))

        #
        if command == CameraServer.COMMAND_PING:
            # no further communication, nothing to return - just indicate that there was no error
            return None

        elif command == CameraServer.COMMAND_GET:
            socket.msend(dh.network.ExtendedJsonSocketMessageType(), kwargs["keys"])
            return socket.mrecv(dh.network.ExtendedJsonSocketMessageType())

        elif command == CameraServer.COMMAND_SET:
            # send dict (keys name the attribute to set) and return dict with the same keys as the sent dict, and each value indicates the success of the operation for its specific key
            socket.msend(dh.network.ExtendedJsonSocketMessageType(), kwargs["values"])
            return socket.mrecv(dh.network.ExtendedJsonSocketMessageType())

        elif command == CameraServer.COMMAND_CAPTURE:
            # send params dict and receive and return image as byte array (contains contents of the encoded image file)
            socket.msend(dh.network.ExtendedJsonSocketMessageType(), kwargs["params"])
            b = socket.mrecv(dh.network.ByteSocketMessageType())
            return b

    def ping(self):
        t0 = time.time()
        self.query(command=CameraServer.COMMAND_PING)
        t1 = time.time()
        return t1 - t0

    def set(self, **values):
        return self.query(command=CameraServer.COMMAND_SET, values=values)

    def get(self, *keys):
        return self.query(command=CameraServer.COMMAND_GET, keys=keys)

    def _getSingle(self, key):
        return self.get(key)[key]

    def capture(self, params={}):
        b = self.query(command=CameraServer.COMMAND_CAPTURE, params=params)
        I = dh.image.decode(b)
        return I

    def save(self, filename, params={}):
        """
        Capture an image an save it directly to file. This is faster than using
        `capture()` and saving the NumPy matrix afterwards, because the here
        the image does not have to be decoded and re-encoded again.
        """
        b = self.query(command=CameraServer.COMMAND_CAPTURE, params=params)
        with open(filename, "wb") as f:
            f.write(b)

    @property
    def brightness(self):
        return self._getSingle("brightness")

    @property
    def framerate(self):
        return self._getSingle("framerate")

    @property
    def resolution(self):
        return self._getSingle("resolution")
