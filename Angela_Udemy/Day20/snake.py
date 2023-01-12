from turtle import Turtle
starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
right = 0
left = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for n in starting_position:
            self.add_segments(n)

    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for n in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[n-1].xcor()
            new_y = self.segments[n-1].ycor()
            self.segments[n].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.segments[0].heading() != down:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != up:
            return self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != right:
            return self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != left:
            return self.segments[0].setheading(0)





















