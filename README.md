# PC UART Video Receiver & Visualizer

A small Python tool to receive and display raw video frames sent over UART from an embedded device. Useful for visualizing video output during testing, especially when working with low-latency streams on microcontrollers.

## What it does

- Connects to a serial port and listens for incoming video data  
- Reconstructs video frames from the stream  
- Displays those frames in a window in (mostly) real-time  
- Optionally logs frame timing and stats to help with debugging

## Project layout (subject to change)

```
uart_video_visualizer/
├── main.py             # Script entry point
├── serial_reader.py    # Handles UART communication
├── frame_parser.py     # Parses raw bytes into image frames
├── utils/              # Helpers for stats, logging, etc.
└── README.md
```

## Goals

- Build a lightweight, cross-platform tool for serial video visualization  
- Support basic video formats like grayscale or RGB565  
- Keep it modular enough to tweak for different microcontroller setups

## To-Do (not started)

- [ ] Set up serial communication and basic CLI config (port, baud, etc.)  
- [ ] Define a frame protocol or delimiter system for clean parsing  
- [ ] Implement basic frame parser (grayscale first, then possibly RGB)  
- [ ] Create a simple display window for the video stream  
- [ ] Add frame timing/stats logging (FPS, dropped frames, etc.)  
- [ ] Gracefully handle errors or misaligned data  
- [ ] Optional: record video to file for later playback  
- [ ] Optional: support multiple frame sizes or resolutions  
- [ ] Optional: develop a basic GUI or overlay for interaction  
