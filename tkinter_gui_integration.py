from tkinter import *
import sys
import time
import pyautogui
import threading
root = Tk()

checkbutton_val = BooleanVar()
slider_val = IntVar()
def enablejiggle():
    if checkbutton_val.get() == False:
        slider.set(0)
    if checkbutton_val.get() == True:
        slider.set(10)
        # threading.Thread(target=jiggle, daemon=True).start()
    mouse_time = slider.get()
    # print(mouse_time)

# def jiggling():
#     time.sleep(mouse_time)
#     pyautogui.moveRel(1, 1)
#     time.sleep(mouse_time)
#     pyautogui.moveRel(-1, -1)

def sliderfunction(value):

   if slider_val.get() == 0:
       checkbutton_val.set(False)
   else:
       checkbutton_val.set(True)
       threading.Thread(target=jiggle, daemon=True).start()
   mouse_time = slider.get()
   print(mouse_time)


def jiggle():
    while True:
       mouse_time = slider.get()
       if mouse_time > 0:
           print('inside while loop')
           time.sleep(mouse_time)
           pyautogui.moveRel(10, 10)
           time.sleep(mouse_time)
           pyautogui.moveRel(-10, -10)




#creating a label or field widget using grid method
mylabel1 = Label(root, text="Enable Jiggle ?", pady=10)
checkbox1 = Checkbutton(root, padx=50, command=enablejiggle, variable=checkbutton_val)

mylabel1.grid(row = 0, column = 0)
checkbox1.grid(row = 0, column = 1)

# integrating slider in the bottom
slider = Scale(root, from_=0, to=60, orient=HORIZONTAL, sliderlength=15, width=15, tickinterval=10, length=270, resolution= 10, command = sliderfunction, variable=slider_val)
slider.grid(row=1,columnspan=2)

seconds = Label(root, text="seconds")
seconds.grid(columnspan=2, row=2)

root.geometry("300x150")
root.title("Mouse Jiggler")
root.resizable(False, False)
root.mainloop()