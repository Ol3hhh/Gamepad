import serial
import time
import pyautogui

try:
    ser = serial.Serial('COM6', 9600, timeout=1)
    print("Connected")
except Exception as e:
    print("Connection error:", e)
    exit(1)

time.sleep(2)

center_x1 = 512
center_y1 = 512
center_x2 = 512
center_y2 = 512

move_threshold = 8
mouse_scale = 0.05

scroll_threshold = 25
scroll_scale = 0.1
scroll_cooldown = 0.05
last_scroll_time = 0

button_keys = ['a', 'b', 'c', 'd', 'e', 'f']
button_KEYS = ['A', 'B', 'C', 'D', 'E', 'F']
button_states = [1] * 6
button_last_release = [0] * 6
double_click_threshold = 0.4
last_sw1 = 1
last_sw2 = 1

while True:
    try:
        raw_line = ser.readline()
        if not raw_line:
            continue

        line = raw_line.decode('utf-8', errors='ignore').strip()
        data = list(map(int, line.split(',')))
        if len(data) != 12:
            continue

        x1, y1, sw1 = data[0], data[1], data[2]
        x2, y2, sw2 = data[3], data[4], data[5]
        buttons = data[6:]

        # ruch myszki
        dx = x1 - center_x1
        dy = center_y1 - y1
        if abs(dx) > move_threshold or abs(dy) > move_threshold:
            pyautogui.moveRel(int(dx * mouse_scale), int(dy * mouse_scale), duration=0)

        # skrol
        scroll_input = x2 - center_x2
        current_time = time.time()
        if abs(scroll_input) > scroll_threshold and (current_time - last_scroll_time > scroll_cooldown):
            pyautogui.scroll(int(-scroll_input * scroll_scale))
            last_scroll_time = current_time

        # click myszką
        if sw1 == 0 and last_sw1 == 1:
            pyautogui.mouseDown(button='left')
        elif sw1 == 1 and last_sw1 == 0:
            pyautogui.mouseUp(button='left')
        last_sw1 = sw1

        if sw2 == 0 and last_sw2 == 1:
            pyautogui.mouseDown(button='right')
        elif sw2 == 1 and last_sw2 == 0:
            pyautogui.mouseUp(button='right')
        last_sw2 = sw2

        # double click
        for i in range(6):
            if buttons[i] == 0 and button_states[i] == 1:
                now = time.time()
                if now - button_last_release[i] < double_click_threshold:
                    pyautogui.press(button_KEYS[i])
                else:
                    pyautogui.keyDown(button_keys[i])
                button_states[i] = 0

            elif buttons[i] == 1 and button_states[i] == 0:
                pyautogui.keyUp(button_keys[i])
                button_last_release[i] = time.time()
                button_states[i] = 1

    except Exception as e:
        print(f"Error: {e}")
