from tkinter import *

root = Tk()

#creating a label or field widget using grid method
mylabel1 = Label(root, text="Enable Jiggle ?")
mylabel2 = Label(root, text="Advanced Time Settings")
checkbox1= Checkbutton(root, padx = 50)
checkbox2= Checkbutton(root, padx = 50)

mylabel1.grid(row = 0, column = 0)
checkbox1.grid(row = 0, column = 1)

mylabel2.grid(row = 1, column = 0)
checkbox2.grid(row = 1, column = 1)

root.geometry("300x150")
root.title("Mouse Jiggler")
root.resizable(False, False)
root.mainloop()