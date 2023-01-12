from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
check = {1: "✓", 2: "✓ ✓", 3: "✓ ✓ ✓", 4: "✓ ✓ ✓ ✓"}
check_reps = 1
timer = None

########################################## WE CAN USE WHILE LOOP IN EVENT DRIVEN PROGRAMS WE NEED SOMETHING ELSE




# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global check_reps
    global reps
    reps = 1
    check_reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global check_reps
    work_sec = WORK_MIN * 60
    work_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in [1, 3, 5, 7]:
        count_down(work_sec)
        timer_label.config(text="Timer",  fg=GREEN)



    elif reps in [2, 4, 6]:
        count_down(work_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
        check_label.config(text=f"{check[check_reps]}", bg=YELLOW, font=24)
        check_reps += 1


    elif reps == 8:
        count_down(long_break_sec)
        check_label.config(text="✓", bg=YELLOW, font=24)
        timer_label.config(text="Long Break", fg=RED)
        check_label.config(text=f"{check[4]}", bg=YELLOW, font=24)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time

def count_down(count):
    global timer
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_min == 0:
        count_min = "00"
    elif count_min < 10:
        count_min = f"0{count_min}"

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")    # item config reconfigures the item
    if count > 0:
        timer = window.after(10, count_down, count - 1)
    else:
        reps += 1

        return start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=200, pady=224, bg=YELLOW)


#########    "fg" for foreground

# CANVAS
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # reading image
canvas.create_image(100, 112, image=tomato_img)             # 100 and 112 are x and y values
timer_text = canvas.create_text(100, 130, text ="00.00", fill="white", font=(FONT_NAME, 38, "bold"))
canvas.grid(column=1, row=2)


# MAIN LABEL
timer_label = Label(text="Timer", font=(FONT_NAME, 24, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=1)

# START BUTTON
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

# RESET BUTTON
reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=3)

# ADD CHECKS SIGNS
check_label = Label()
check_label.grid(column=1, row=4 )



window.mainloop()