import time
import serial
from PIL import Image, ImageSequence

HEADER = b'\xAA\x55'
FOOTER = b'\x55\xAA'
FPS = 10
FRAME_DELAY = 1.0/ (FPS)
WIDTH, HEIGHT = 160, 120

gif = Image.open("test.gif")
ser = serial.Serial("COM4", 921600)  # change this port to match setup

while True:
	for frame in ImageSequence.Iterator(gif):
		gray = frame.convert("L").resize((WIDTH, HEIGHT))
		ser.write(HEADER + gray.tobytes() + FOOTER)
		time.sleep(FRAME_DELAY)
