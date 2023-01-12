########################## TURTLE OBJECTS #################
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)      # window size


all_turtles = []
colors = ["red", "yellow", "green", "blue", "orange", "purple"]

for i in range(6):
    the_turtle = Turtle(shape="turtle")
    the_turtle.color(colors[i])
    all_turtles.append(the_turtle)

bet = screen.textinput(title="make you bet", prompt="Enter the color of you bet turtle")

y_axis = -100
for n in all_turtles:
    n.penup()
    n.goto(-230, y_axis)
    y_axis += 40

game_on = True
while game_on == True:
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 220:                                                     # returns x coordinate
            game_on = False
            winner_color = turtle.pencolor()        # it sets or returns the color
            if winner_color == bet:
                print(f"You've won! The {winner_color} is the winner")
            else:
                print(f"You've lost! The {winner_color} is the winner")

screen.exitonclick()

