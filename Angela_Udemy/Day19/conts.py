import turtle
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def move_back():
    tim.back(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")  # (HIGHER ORDER) FUNCTION IS USED AS INPUT (move_forward)  only NO parenthesis !!!!!!!!!!
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_back, "s")
screen.onkey(clear, "space")
screen.exitonclick()


