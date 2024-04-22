from tkinter import *
import time
import pyautogui
import threading

root = Tk()

checkbutton_val = BooleanVar()
slider_val = IntVar()

def enable_jiggle():
    if not checkbutton_val.get():
        slider.set(0)
    else:
        slider.set(10)

def jiggle_mouse():
    while True:
        mouse_time = slider.get()
        time.sleep(mouse_time)
        pyautogui.moveRel(1, 1)
        time.sleep(mouse_time)
        pyautogui.moveRel(-1, -1)

def slider_function(value):
    if slider_val.get() == 0:
        checkbutton_val.set(False)
    else:
        checkbutton_val.set(True)
        if int(value) > 0:  # Start jiggling only if slider value is greater than 0
            threading.Thread(target=jiggle_mouse, daemon=True).start()

my_label = Label(root, text="Enable Jiggle ?", pady=10)
checkbox = Checkbutton(root, padx=50, command=enable_jiggle, variable=checkbutton_val)
my_label.grid(row=0, column=0)
checkbox.grid(row=0, column=1)

slider = Scale(root, from_=0, to=60, orient=HORIZONTAL, sliderlength=15, width=15, tickinterval=10, length=270, resolution=10, command=slider_function, variable=slider_val)
slider.grid(row=1, columnspan=2)

seconds = Label(root, text="seconds")
seconds.grid(columnspan=2, row=2)

root.geometry("300x200")
root.title("Mouse Jiggler")
root.resizable(False, False)
root.mainloop()
