import pyautogui
import time
while True:
    try:
        print(pyautogui.position())
        time.sleep(1)
    except Exception as e:
        print(e)