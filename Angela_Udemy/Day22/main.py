from turtle import Screen
from paddles import Paddles
from turtle import Turtle
import time
from ball import Ball

paddles = Paddles()
screen = Screen()
line = Turtle()
ball = Ball()

screen.setup(1500, 800)
screen.bgcolor("black")
screen.title("Pong Arcade")


line.color("white")
line.shape("square")
line.speed("fastest")
line.penup()
line.goto(0, 400)
line.setheading(270)


for i in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(20)

screen.listen()
screen.onkey(paddles.p1_up, "w")
screen.onkey(paddles.p1_down, "s")

screen.onkey(paddles.p2_up, "i")
screen.onkey(paddles.p2_down, "k")
ball.move()

ball.ball[0].setheading(45)
game_on = True

while game_on:
    ball.move()




# screen.listen()
# screen.onkey(paddle1.up, "w")
# screen.onkey(paddle1.down, "s")
#
# screen.onkey(paddle2.up, "i")
# screen.onkey(paddle2.down, "k")


screen.exitonclick()