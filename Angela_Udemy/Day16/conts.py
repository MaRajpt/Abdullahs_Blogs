#####################  OOP ( Turtle Graphics ) #############################

from turtle import Turtle, Screen       ## importng classes from turtle module
import another_module
# print(another_module.another_variable)
#
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.color('coral')
#
# my_screen = Screen()
# print(my_screen.canvheight)     # canvheight is attribute
# my_screen.exitonclick()

from prettytable import PrettyTable   # Manualy downloaded this PACKAGE

table = PrettyTable()
table.add_column('City', ['a','b','c','d'])
table.add_column('Code', [100,200,300,400])  # same lenght of colums otherwise error
#change table style with atrributes

table.align = "r"       # changing the attributes

print(table)



