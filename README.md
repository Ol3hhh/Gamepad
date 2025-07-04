# Gamepad Controller with Arduino and Python

This project implements a custom gamepad controller using **Arduino** and a **Python interface** for PC interaction.  
It reads input from joysticks and buttons via analog and digital pins, and maps those signals to keyboard or mouse actions on the computer.

## Features

- Arduino-based joystick and button input
- Serial communication with a Python script
- Python script controls keyboard (via `pyautogui`)
- Support for mouse movement, button presses, scrolling
- Basic double-click and debounce logic
- Works with games or desktop applications

## Components

- 2 analog joysticks (X/Y + push-button)
- 6 digital buttons
- Arduino (e.g., Uno, Mega)
- Python environment with `pyserial`, `pyautogui`

## File Structure

Gamepad/
├── ino/
│ └── sketch_jun11a.ino # Arduino sketch (reads joystick + button input)
├── py/
│ ├── arduino_keyboard.py # Serial-to-keyboard/mouse mapper
│ └── mortal_kombat.py # Example interaction or custom mapping


## Requirements

### Hardware:
- Arduino-compatible board
- USB connection to PC
- Joysticks + buttons

### Software:
- Arduino IDE
- Python 3.x
- Python packages:
  ```bash
  pip install pyserial pyautogui
'''
- Vjoy
