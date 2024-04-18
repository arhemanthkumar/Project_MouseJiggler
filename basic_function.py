import sys
import time

import pyautogui
print(pyautogui.size())

enable_jiggle = True
mouse_time = 5

while enable_jiggle:
    try:
        time.sleep(mouse_time)
        pyautogui.moveRel(1,1)
        time.sleep(mouse_time)
        pyautogui.moveRel(-1,-1)
    except KeyboardInterrupt:
        # enable_jiggle = False
        pass
