import serial
import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True, help="Serial port (e.g. COM3 or /dev/ttyUSB0)")
parser.add_argument("--width", type=int, required=True)
parser.add_argument("--height", type=int, required=True)
args = parser.parse_args()

ser = serial.Serial(args.port, 115200)

frame_size = args.width * args.height

while True:
    data = ser.read(frame_size)
    frame = np.frombuffer(data, dtype=np.uint8).reshape((args.height, args.width))
    cv2.imshow("UART Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ser.close()
cv2.destroyAllWindows()
