
class Game:
    def __init__(self):
        self.update_score()
        self.player_score = int(self.read_file())


    def read_file(self):
        with open("score.txt") as score:
            get_score = score.read()
            return get_score


    def update_score(self):
        with open("score.txt", "w") as score:
            score.write("4")


game = Game()


print(type(game.player_score))
