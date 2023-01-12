from turtle import Turtle, Screen
import pandas as pd
import turtle as state_location
file = pd.read_csv("50_states.csv")
states = []
for i in file.state:
    states.append(i)

turtle = Turtle()
state_location = Turtle()

screen = Screen()
screen.title("U.S States GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

game_on = True
correct_answers = []
while game_on == True:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50", prompt="Whats another states name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        correct_answers.append(answer_state)
        axis = file[file.state == answer_state]
        x_axis = int(axis.x)
        y_axis = int(axis.y)
        state_location.penup()
        state_location.hideturtle()
        state_location.goto(x_axis, y_axis)
        # instead of using {answer_state} we can use use fi
        state_location.write(f"{answer_state}", move=False, align='left', font=('Arial', 8, 'normal'))

# states to learn.csv




screen.onscreenclick(get_mouse_click_coor)
screen.mainloop()


