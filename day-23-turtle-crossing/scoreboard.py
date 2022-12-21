from turtle import Turtle

FONT = ("Courier", 12, "normal")
GAME_OVER = ("Courier", 30, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.level_written()

    def level_written(self):
        self.clear()
        self.penup()
        self.goto(-250, 270)
        self.hideturtle()
        self.write(f'Level : {self.level}', align='Center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.level_written()

    def write_gameover(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write('Game Over', align='Center', font=GAME_OVER)



