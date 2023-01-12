from turtle import Turtle
import random

class Ball:
    def __init__(self):
        self.ball = []
        self.make_ball()

    def make_ball(self):
        one_ball = Turtle()
        one_ball.shape("circle")
        one_ball.color("red")
        one_ball.shapesize(2, 2)
        one_ball.penup()
        one_ball.goto(0, random.randint(-300, 300))
        one_ball.penup()
        self.ball.append(one_ball)

    def move(self):
        self.ball[0].forward(10)
        if self.ball[0].ycor() > 370:
            self.speed("fastest")
            self.ball[0].setheading(315)
            self.ball[0].forward(10)




