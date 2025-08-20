# PC UART Video Receiver & Visualizer
Minimal Python scripts to test sending and receiving raw grayscale video frames over UART.  

## Current Status
- **viewer.py**  
  - Connects to a serial port  
  - Reads fixed-size grayscale frames (width/height from CLI)  
  - Displays frames in a window  

- **dummy_sender.py**  
  - Reads frames from a GIF  
  - Converts them to grayscale  
  - Streams them over UART with a fixed delay  

This demonstrates the flow: **GIF → UART → PC Viewer**.

## Current Layout
```
uart_video_visualizer/
├── viewer.py 		# UART video viewer (reads and displays frames)
├── gif_test.py 	# sends GIF frames over UART for testing
└── README.md
```

## Goals
- Provide a minimal starting point for UART video visualization  
- Incrementally add structure (protocol, parsing, error handling) in later iterations  
- Keep the code modular enough for different microcontroller setups  

## To-Do
- [x] Minimal serial setup and basic read/write loop  
- [ ] Add header/footer protocol for frame sync  
- [ ] Improve reshape and add dropped frame counter  
- [ ] Error handling and resync logic  
- [ ] Visualization improvements (beyond grayscale)  
- [ ] Optional: recording, stats, GUI  
