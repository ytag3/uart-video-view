import argparse
import serial
import numpy as np
import cv2

HEADER = b'\xAA\x55'
FOOTER = b'\x55\xAA'

# checks frame boundaries
def read_frame(ser, width, height):
	frame_size = width * height

	#sync to header recieved
	stream_data = ser.read(2)
	while stream_data != HEADER:
		stream_data = stream_data[1:] + ser.read(1)

	#read frame data
	frame_bytes = ser.read(frame_size)

	#check footer
	footer = ser.read(2)
	if footer != FOOTER:
		print("Bad footer, frame skipped")
		return None

	frame = np.frombuffer(frame_bytes, dtype=np.uint8).reshape((height, width))
	return frame

def main():
	parser = argparse.ArgumentParser(description="UART Video Visualizer")
	parser.add_argument("--port", required=True, help="Serial port")
	parser.add_argument("--baud", type=int, default = 115200, help="Baud Rate")
	parser.add_argument("--width", type=int, default = 160)
	parser.add_argument("--height", type=int, default = 120)
	args = parser.parse_args()

	ser = serial.Serial(args.port, args.baud, timeout=1)

	while True:
		frame = read_frame(ser, args.width, args.height)
		if frame is not None:
			cv2.imshow("UART video",frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	ser.close()
	cv2.destroyAllWindows()

if __name__ ==" __main__":
	main()
