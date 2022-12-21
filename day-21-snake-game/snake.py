from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segment = []
        self.createsnake()
        self.head = self.segment[0]

    def createsnake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.up()
        new_turtle.goto(position)
        self.segment.append(new_turtle)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range((len(self.segment)-1), 0, -1):
            new_x = self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(10)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.createsnake()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)