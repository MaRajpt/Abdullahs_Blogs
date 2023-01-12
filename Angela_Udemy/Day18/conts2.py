from turtle import Turtle, Screen
from random import *
from turtle import *
tim = Turtle()
scr = Screen()

tim.shape("turtle")
#tim.color("red")


# for n in range(5):                  # draw DASHED LINE
#     tim.forward(50)
#     tim.penup()
#     tim.forward(50)
#     tim.pendown()


###################  DRAWING  SHAPES< WITH VARIOUS SIDES
import random


#
# def draw_shape(sides):
#     angle = 360/sides
#     for n in range(sides):
#         tim.forward(100)
#         tim.left(angle)
#
# for side in range(3, 11):
#     tim.pensize(8)
#     tim.color(random.choice(colors))
#     draw_shape(side)
#


############################   RANDOM WALK
colormode(255)

def random_c():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rc = (r, g, b)
    return rc

# angle = [0, 90, 180, 270]
# tim.pensize(7)
# tim.speed(50)
#
# for n in range(150):
#     tim.color(random_c())
#     tim.forward(50)
#     tim.right(random.choice(angle))


############### CIRCLE


def draw_spirograph(size_of_gap):

    for i in range(int(360/ size_of_gap)):

        tim.color(random_c())

        tim.speed(100)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        # tim.left(10)

draw_spirograph(5)



scr.exitonclick()




















