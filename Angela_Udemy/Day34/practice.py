# from tkinter import *
#
#
# class QuizInterface(Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("744x377")
#         self.mybutton = Button(text="press", command=self.click).pack()
#
#     def status(self):
#         self.var = StringVar()
#         self.var.set("Ready")
#         self.statusbar = Label(self, relief=SUNKEN, anchor="w")
#         self.statusbar.pack(side=BOTTOM, fill=X)
#
#     def click(self):
#         print("Button clicked")
#
#
#
# if __name__ == '__main__':
#     window = QuizInterface()
#     window.status()
#     window.createbutton("Click me")
#     window.mainloop()


# x = 2.3
#
# print(int(x))


x = 'True'

y = True

if bool(x) == y:
    print("equals")