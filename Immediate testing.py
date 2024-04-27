from tkinter import *
import time
import pyautogui
import threading
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()


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
mylabel1 = customtkinter.CTkLabel(root, text="Enable Jiggle ?", anchor="w",font=('Times', 20))
checkbox1 = customtkinter.CTkCheckBox(root, text="", command=enablejiggle, variable=checkbutton_val)

mylabel1.grid(row=1, column=0,  padx = 15, pady=10, columnspan=2)
checkbox1.grid(row=1, column=2, padx=100, pady=10, sticky="ew", columnspan=2)

# integrating slider in the bottom
slider = customtkinter.CTkSlider(root, from_=0, to=60, width=250,  number_of_steps=6,
                command=sliderfunction, variable=slider_val)
slider.grid(row=2, columnspan=3, pady=10)

mylabel2 = customtkinter.CTkLabel(root, text=" 0   10    20    30    40    50    60", anchor="center",font=('Times', 20))
mylabel2.grid(row=3, column=0,  columnspan=3)

seconds = customtkinter.CTkLabel(root, text="seconds", font=('Times', 20), anchor="center")
seconds.grid(row = 4,columnspan = 3, pady=5)



ico = Image.open('icon.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

root.geometry("310x150")
root.title("Mouse Jiggler")
root.resizable(False, False)
root.mainloop()
