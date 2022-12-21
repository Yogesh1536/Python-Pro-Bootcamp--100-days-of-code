from turtle import Turtle


UP = 90
DOWN = 270


class Padle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.createpadle()
        self.setpos(position)

    def createpadle(self):
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color('white')
        self.penup()
        self.up()
        self.down()

    def up(self):
        self.setheading(UP)
        self.forward(20)

    def down(self):
        self.setheading(DOWN)
        self.forward(20)


