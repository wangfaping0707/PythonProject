#!D:\PythonProject\venv\Scripts\python.exe

import argparse

import picamera

import dh.hardware.raspi


def main():
    parser = argparse.ArgumentParser(description="Starts a server providing remote access to the Raspberry Pi camera.")
    parser.add_argument("-p", "--port", default=7220, help="Port to be used for the server.")
    args = parser.parse_args()

    with picamera.PiCamera() as camera:
        S = dh.hardware.raspi.CameraServer(camera=camera, port=args.port)
        S.run()


if __name__ == "__main__":
    main()
