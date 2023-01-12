from tkinter import*
window = Tk()

window.title("My first GUI ")
window.minsize(500, 300)
window.config(padx=100, pady=200)


#Label

my_lable = Label(text="I'm a label", font=('Arial', 24, "bold"))
# my_lable["text"] = "New Text"       # dictionary
my_lable.config(text="New Text")   # BOTH SAME
my_lable.grid(column=0, row=0)

#Button 1
def button1_click():
    print("I got clicked")
    my_lable["text"] = input.get()
button1 = Button(text="Click me", command=button1_click)
button1.grid(column=1, row=1)

#Button 2
def button2_click():
    print("I got clicked")
    my_lable["text"] = input.get()
button2 = Button(text="Click me", command=button2_click)
button2.grid(column=2, row=0)

#Entry

input = Entry(width=10)
print(input.get())          # return the input string
input.grid(column=3, row=2)















window.mainloop()   # built in loop to keep window open  ( at end of program )