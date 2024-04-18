print("this is for testing only")

import time

import pyautogui
print(pyautogui.size())

time.sleep(5)
pyautogui.moveTo(1000,300,duration=1) #moves in number of pixels in x and y direction along with duration
# pyautogui.moveRel(500,500,duration=1) #relative mouse movement from the position
print(pyautogui.position())

# pyautogui.click(80,30,duration=1)
# pyautogui.click(80,70,duration=0.5)

pyautogui.scroll(-500)
time.sleep(1)
pyautogui.scroll(500)


pyautogui.click(1000,110,duration=1)
pyautogui.typewrite("iPhone")
pyautogui.click(1380,110,duration=1)
pyautogui.click(1000,110,duration=1)
pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("ctrl","c")

pyautogui.hotkey("ctrl","t")
pyautogui.hotkey("ctrl","v")
pyautogui.click()