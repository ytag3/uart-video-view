import serial
import time
import numpy as np
from PIL import Image

ser = serial.Serial("COM4", 115200)  # change this port to match your setup

gif = Image.open("test.gif")

while True:
    try:
        gif.seek(gif.tell() + 1)
    except EOFError:
        gif.seek(0)

    gray = gif.convert("L")
    arr = np.array(gray)

    ser.write(arr.tobytes())
    time.sleep(0.1)
