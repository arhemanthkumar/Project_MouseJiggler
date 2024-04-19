import os
from tkinter import *
root = Tk()

e = Entry(root, width=20, borderwidth=5, font=('TimesNewRoman 15'))
e.grid(row=0, column=0, columnspan=3, padx=15, pady=15, ipadx=20, ipady=10)

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def bclear():
    e.delete(0, END)

def bplus():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    f_num = int(first_num)
    global operation
    operation = "addition"

def bequal():
    second_num = e.get()
    e.delete(0,END)
    if operation == "addition":
        e.insert(0, f_num + int(second_num))
    if operation == "multiplication":
        e.insert(0, f_num * int(second_num))
    if operation == "subtraction":
        e.insert(0, f_num - int(second_num))
    if operation == "division":
        e.insert(0, f_num / int(second_num))

def bmult():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    f_num = int(first_num)
    global operation
    operation = "multiplication"


def bsub():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    f_num = int(first_num)
    global operation
    operation = "subtraction"


def bdiv():
    first_num = e.get()
    e.delete(0, END)
    global f_num
    f_num = int(first_num)
    global operation
    operation = "division"


button1 = Button(root, text="1", padx = 40, pady = 20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx = 40, pady = 20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx = 40, pady = 20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx = 40, pady = 20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx = 40, pady = 20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx = 40, pady = 20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx = 40, pady = 20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx = 40, pady = 20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx = 40, pady = 20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx = 40, pady = 20, command=lambda: buttonClick(0))

button_clear = Button(root, text="CLEAR",padx=72, pady=20, command=bclear)
button_plus = Button(root, text="+",padx=38, pady=20, command=bplus)
button_equal = Button(root, text="=", padx=91, pady=20, command=bequal)

button_multiply = Button(root, text="*",padx=40, pady=20, command=bmult)
button_subtract = Button(root, text="-",padx=41, pady=20, command=bsub)
button_divide = Button(root, text="/",padx=41, pady=20, command=bdiv)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_multiply.grid(row=6, column=0)
button_subtract.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.title("Simple Calculator")

root.mainloop()