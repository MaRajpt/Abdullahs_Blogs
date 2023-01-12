from turtle import Turtle , Screen

position = [(700, 0), (-700, 0)]
move = 50

class Paddles:
    def __init__(self):
        self.paddle_pair = []
        self.create_paddle()


    def create_paddle(self):
        for i in position:
            one_paddle = Turtle()
            one_paddle.speed("fastest")
            one_paddle.shape("square")
            one_paddle.color("blue")
            one_paddle.setheading(90)
            one_paddle.shapesize(3, 15)
            one_paddle.penup()
            one_paddle.goto(i)
            self.paddle_pair.append(one_paddle)

    def p1_up(self):

        self.paddle_pair[1].forward(move)

    def p1_down(self):
        self.paddle_pair[1].backward(move)

    def p2_up(self):
        self.paddle_pair[0].forward(move)

    def p2_down(self):
        self.paddle_pair[0].backward(move)
