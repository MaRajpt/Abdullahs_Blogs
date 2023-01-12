#//////////////////// GRAPHICAL USER INTERFACE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#  "Tkinter" is python tool to create GUIs
# Tkinter is standard library in python for creating GUI for desktop application
# Toolkit used will be Tk, pythons default gui library
# access it by Tk interface

from tkinter import*

win = Tk()

win.geometry("200x100")

b = Button(win, text= "Submit")

b.pack()
win.mainloop()