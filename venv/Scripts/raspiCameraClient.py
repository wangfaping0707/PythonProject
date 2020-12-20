#!D:\PythonProject\venv\Scripts\python.exe

import argparse
import json
import re

import dh.utils
import dh.image
import dh.hardware.raspi


def main():
    # parse arguments
    parser = argparse.ArgumentParser(
        description="Starts a client for remote access to a Raspberry Pi camera server and shows a live video.",
        epilog="Example: raspiCameraClient.py 127.0.0.1 --set=resolution:'(640,480)' --set=vflip:true --set=hflip:true"
    )
    parser.add_argument("host", type=str, help="Host (hostname or IP address) of the server to connect to.")

    parser.add_argument("-p", "--port", type=int, default=7220, help="Port of the server to connect to.")
    parser.add_argument("-s", "--set", action="append", metavar="<KEY>:<VALUE>", help="Allows to specify camera settings via key-value pairs. Each value must be a JSON-formatted string (see example). Can be specified multiple times.")
    args = parser.parse_args()

    # start client
    C = dh.hardware.raspi.CameraClient(host=args.host, port=args.port)

    # apply initial settings
    values = {}
    if args.set is not None:
        for keyValueStr in args.set:
            m = re.match("^([a-zA-Z0-9_-]+):(.+)$", keyValueStr)
            if m is None:
                raise ValueError("Invalid format for set: must be '<key>:<value>' (got '{}')".format(keyValueStr))
            (key, valueStr) = m.groups()
            try:
                value = json.loads(valueStr)
            except:
                value = valueStr
            values[key] = value
        if len(values) > 0:
            print("** SET request:")
            result = C.set(**values)
            rows = [[key, values[key], result[key]] for key in sorted(result.keys())]
            dh.utils.ptable(rows, headers=["Attribute", "Value", "Response"])
            print("")

    #
    F = dh.utils.FrequencyEstimator()
    run = True
    key = ord(" ")
    while run:
        try:
            if key in dh.utils.qkeys():
                return
            elif key == ord(" "):
                print("** GET request:")
                info = C.get(*dh.hardware.raspi.CameraServer.GET_SET_ATTRIBUTES)
                rows = [[key, info[key]] for key in sorted(info.keys())]
                dh.utils.ptable(rows, headers=["Attribute", "Value"])
                print("")

            # capture image
            params = {}
            I = C.capture(params)

            # show image (with FPS and ping)
            dh.image.text(I, "{} fps".format(dh.utils.around(F.event())), position=(0.0, 0.0), anchor="lt")
            dh.image.text(I, "ping: {} ms".format(dh.utils.around(C.ping() * 1000.0)), position=(1.0, 0.0), anchor="rt")
            dh.image.text(I, "{}:{}".format(args.host, args.port), position=(0.0, 1.0), anchor="lb")
            key = dh.image.show(I, wait=10)
        except KeyboardInterrupt:
            # prevent keyboard interrupts within the communication with the server - instead, finish communication and exit gracefully
            print("Exiting gracefully...")
            run = False


if __name__ == "__main__":
    main()
