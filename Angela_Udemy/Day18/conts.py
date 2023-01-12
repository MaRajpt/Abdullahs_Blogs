from turtle import Turtle, Screen
from turtle import *   # * to import every thing from turtle module ( BUT CAN BE CONFUSING )

# import hooa_looita_kobodao_pupu as hello   ( IF a module name is really long an alias can be given to it e.g hello ( import .... as hello)
# t = hello


tt = Turtle()
tt.shape("turtle")
tt.color("red")

for t in range(4):
    tt.forward(100)  # 100 Places       # MAKE A SQUARE
    tt.right(90)  # 90 %


import heroes                       #  heros is not pytho ndafault module hence need installation
print(heroes.gen())



screen = Screen()
screen.exitonclick()



