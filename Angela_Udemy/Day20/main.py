            ##################### SNAKE GAME ( MAIN )#######################

from snake import Snake
import time
from turtle import Screen
from food import Food
from score import Score


food = Food()
screen = Screen()
snake = Snake()
score = Score()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Snake Game")
screen.tracer(0)
game_score = 0

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food  using Turtle distance method

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.score_increament()
        snake.extend()

    # detect collision with wall.
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -290:
        game_on = False
        score.game_over()

    # detect collision with tail.
    #   """"USING PYTHON SLICING ""

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_on = False
            score.game_over()

            screen.exitonclick()

