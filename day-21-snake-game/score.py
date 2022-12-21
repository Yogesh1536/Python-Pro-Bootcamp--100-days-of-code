from turtle import Turtle

FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as high_score:
            self.highscore = int(high_score.read())
        self.color('white')
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'score : {self.score}  Highscore : {self.highscore}', align='center', font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
            self.update_scoreboard()
            with open('data.txt', 'w') as high_score:
                high_score.write(str(self.highscore))


    def add_score(self):

        self.score += 1
        self.update_scoreboard()
