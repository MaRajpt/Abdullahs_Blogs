###################### EXTRACT COLORS ################################
# EXTRACT COLORS FROM IMAGE

from turtle import *
import random
# import colorgram
#
# # Extract 6 colors from an image.
#
# rgb_colors = []
# colors = colorgram.extract('dots.jpg', 20)
# for color in colors:
#      r = color.rgb.r
#      b = color.rgb.b
#      g = color.rgb.g
#      rgb_colors.append((r,g,b))
#
# print(rgb_colors)
#
# #############################################
colormode(255)
tim = Turtle()
screen = Screen()


colors = [(55, 30, 20), (205, 135, 112), (6, 13, 29), (152, 81, 48), (47, 93, 145), (236, 211, 92), (199, 97, 74), (94, 167, 203), (149, 70, 93), (162, 160, 60), (166, 137, 161), (38, 84, 50), (124, 33, 22), (191, 89, 108), (28, 57, 34), (117, 195, 174)]
def rc():
    rand_col = random.choice(colors)
    return rand_col

tim.hideturtle()
tim.penup()
pos = tim.goto(-220, -180)
tim.speed(30)
for y in range(1, 11):
    for x in range(10):
        tim.color(rc())
        tim.penup()
        tim.fd(50)
        tim.dot(20)
    tim.goto(-220, -180+50*y)



    # tim.dot(20)
    # tim.forward(20)

screen.exitonclick()

