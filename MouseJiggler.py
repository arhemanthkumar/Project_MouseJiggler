from tkinter import *
import time
import pyautogui
import threading
root = Tk()
from PIL import Image, ImageTk

checkbutton_val = BooleanVar()
slider_val = IntVar()


def enablejiggle():
    if checkbutton_val.get() is False:
        slider.set(0)
    if checkbutton_val.get() is True:
        slider.set(10)


def sliderfunction(value):

    if slider_val.get() == 0:
        checkbutton_val.set(False)
    else:
        checkbutton_val.set(True)
        threading.Thread(target=jiggle, daemon=True).start()
    '''mouse_time = slider.get()
    print(mouse_time)
    used for debugging only -> to check immediate slider value
    '''


def jiggle():
    count = 0
    mouse_time = slider.get()
    while mouse_time > 0:
        if count == mouse_time:
            pyautogui.moveRel(1, 1)
            pyautogui.moveRel(-1, -1)
            count = 0
        count += 1
        time.sleep(1)
        new_mouse_time = slider.get()
        if new_mouse_time != mouse_time:
            count = 0
            mouse_time = new_mouse_time


# creating a label or field widget using grid method
mylabel1 = Label(root, text="Enable Jiggle ?", pady=10,padx=10)
checkbox1 = Checkbutton(root,  command=enablejiggle, variable=checkbutton_val,height=1)

mylabel1.grid(row=0, column=0,sticky=W)
checkbox1.grid(row=0, column=1,sticky=E)

# integrating slider in the bottom
slider = Scale(root, from_=0, to=60, orient=HORIZONTAL, sliderlength=15, width=15, tickinterval=10, length=285,
               resolution=10, command=sliderfunction, variable=slider_val)
slider.grid(row=1, column=0, columnspan=2,padx=10)

seconds = Label(root, text="seconds")
seconds.grid(columnspan=2, row=2)

# ico = Image.open('icon.ico')
# photo = ImageTk.PhotoImage(ico)
# root.wm_iconphoto(False, photo)

root.geometry("310x150")
root.title("Mouse Jiggler")
root.resizable(False, False)
root.mainloop()
