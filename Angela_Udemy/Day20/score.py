from turtle import Turtle

class Score(Turtle):
    def __init__(self):

        super().__init__()
        self.game_score = 0
        self.penup()
        self.hideturtle()
        self.goto((0, 275))
        self.write(f"Score = {self.game_score}", move=False, align='center', font=('courier', 15, 'bold'))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !", move=False, align='center', font=('courier', 30, 'bold'))



    def score_increament(self):
        self.game_score += 1
        self.clear()
        self.write(f"Score = {self.game_score}", move=False, align='center', font=('courier', 15, 'bold'))




