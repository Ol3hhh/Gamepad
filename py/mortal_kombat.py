import serial
import pyvjoy
import time
import signal
import sys

def cleanup():
    try:
        vj.reset()
    except:
        pass
    try:
        ser.close()
    except:
        pass
    sys.exit(0)

signal.signal(signal.SIGINT, lambda sig, frame: cleanup())

try:
    ser = serial.Serial('COM6', 9600, timeout=1)
    print("Connected")
except Exception as e:
    print("Connection error:", e)
    exit(1)

vj = pyvjoy.VJoyDevice(1)

def map_range(val, in_min, in_max, out_min, out_max):
    return int((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if not line:
            continue

        parts = list(map(int, line.split(',')))
        if len(parts) < 12:
            continue

        x1, y1, sw1 = parts[0], parts[1], parts[2]
        x2, y2, sw2 = parts[3], parts[4], parts[5]
        buttons = parts[6:]

        # Lewy joystick
        vj.set_axis(pyvjoy.HID_USAGE_X, map_range(x1, 0, 1023, 0, 32768))
        vj.set_axis(pyvjoy.HID_USAGE_Y, map_range(1023 - y1, 0, 1023, 0, 32768))  # inwersja Y

        vj.set_button(4, 1 if buttons[0] == 0 else 0)  # Y (D2)
        vj.set_button(3, 1 if buttons[1] == 0 else 0)  # B (D3)
        vj.set_button(2, 1 if buttons[2] == 0 else 0)  # A (D4)
        vj.set_button(1, 1 if buttons[3] == 0 else 0)  # X (D5)

        # vj.set_button(11, 1 if buttons[4] == 0 else 0)  # D6
        # vj.set_button(12, 1 if buttons[5] == 0 else 0)  # D7

        # klliknięcia joysticków
        vj.set_button(9, 1 if sw1 == 0 else 0)   # L3 (D8)
        vj.set_button(10, 1 if sw2 == 0 else 0)  # R3 (D25)

        # X LB (lewo), RB (prawo)
        center = 512
        deadzone = 60

        if x2 < center - deadzone:
            vj.set_button(5, 1)  # LB
        else:
            vj.set_button(5, 0)

        if x2 > center + deadzone:
            vj.set_button(6, 1)  # RB
        else:
            vj.set_button(6, 0)

        # Y LT (up) / RT (down)
        if y2 < center - deadzone:
            vj.set_button(7, 1)  # LT
        else:
            vj.set_button(7, 0)

        if y2 > center + deadzone:
            vj.set_button(8, 1)  # RT
        else:
            vj.set_button(8, 0)

    except Exception as e:
        print("Data error:", e)

    time.sleep(0.01)
