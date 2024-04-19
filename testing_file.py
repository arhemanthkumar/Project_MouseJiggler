import time
import tkinter

import pyautogui
import tkinter as tk

"""
in tkiner:
first we create to the root and then we push/pack/deploy/build into the root
"""
root = tkinter.Tk()
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

#creating a label or field widget
myLabel = tk.Label(root, text= "Hello World !")

#packing the label
myLabel.pack()

#window tiling:
root.geometry("350x150")
root.title("Mouse Jiggler")

#creating a label or field widget using grid method
mylabel1 = tk.Label(root, text="Hello World!")
mylabel2= tk.Label(root, text="I am Hemanth Kumar A R")

mylabel1.grid(row = 0, column = 0)
mylabel2.grid(row = 1, column = 0)

"""
we can create buttons:
myButton = tk.Button(root, text = "Click me")
myButton.pack()

also can add padding to buttons or increase or decrease button size by padx and pady and combine packing
myButton = tk.Button(root, text = "Click me", padx = 50, pady = 100).pack()

also can use state=tk.DISABLED to disable the button and state=tk.NORMAL to enable the button

command = defined_function_name with paranthesies -> used to call a function after a click
fg = blue or hex #0000000 or #fffffff -> foreground color
bg = -> background color

put root.resizable(False, False) -> to disable window resize in x and y directions

e = Entry() -> to have a input field in the root
e.get() to display it for example

command=root.quit in button -> to quit the application
root.iconbitmap('directory of the .ico file')

"""

#essential as the GUI starts from the main-loop
root.mainloop()
