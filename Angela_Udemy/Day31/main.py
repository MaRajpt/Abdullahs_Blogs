BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random


# -------------------------------- DATA ARCHIVE--------------------------------------#
try:
    new_file = pandas.read_csv("words_to_learn.csv")
    data = new_file.to_dict(orient="records")  # NEW STUFF to_dict('records')

except FileNotFoundError:
    data_file = pandas.read_csv("/Users/ma088/Desktop/PYTH/Angela_Udemy/Day31/data/french_words.csv")
    data = data_file.to_dict(orient="records")  # NEW STUFF to_dict('records')



# ---------------------------------- DATA GENERATE ---------------------------------#
random_pair = {}


def flip_card(eng):
    canvas.itemconfig(images, image=back_image)
    canvas.itemconfig(title_label, text="English")
    canvas.itemconfig(word_label, text=eng)

def next_card():
    global random_pair
    random_pair = random.choice(data)
    canvas.itemconfig(images, image=front_image)
    canvas.itemconfig(title_label, text="French")
    canvas.itemconfig(word_label, text=random_pair["French"])

# Remember in the mainloop() you should not create additional delayed loops e.g with time.sleep() but instead, used
# window.after()
    window.after(3000, flip_card, random_pair["English"])    ###  after(ms, function ,  *args)

def is_known():
    #------------ UPDATING DATA LIST AND SAVING PROGRESS IN A FILE-------------------#

    data.remove(random_pair)
    update_data = pandas.DataFrame(data)
    update_data.to_csv("words_to_learn.csv", index=False)
    next_card()


#------------------------------ UI -----------------------------------------#
window = Tk()
window.title("flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=525, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="/Users/ma088/Desktop/PYTH/Angela_Udemy/Day31/images/card_front.png")
back_image = PhotoImage(file="/Users/ma088/Desktop/PYTH/Angela_Udemy/Day31/images/card_back.png")
images = canvas.create_image(400, 263, image=front_image)
title_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

wrong_button_image = PhotoImage(file="/Users/ma088/Desktop/PYTH/Angela_Udemy/Day31/images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="/Users/ma088/Desktop/PYTH/Angela_Udemy/Day31/images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()





