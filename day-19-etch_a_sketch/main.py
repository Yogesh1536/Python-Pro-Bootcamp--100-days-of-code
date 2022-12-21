from turtle import Turtle, Screen


pen1 = Turtle()
pen2 = Turtle()
screen = Screen()


def heading():
    pen2.penup()
    pen2.hideturtle()
    pen2.setpos(0, 280)
    pen2.write('press W for move front, S for move back, A for turn anticlockwise and D for turn clockwise',
               align='center', font=['arial', 14, 'normal'])


def forward():
    pen1.forward(10)


def backward():
    pen1.back(10)


def turn_anti_clockwise():
    pen1.left(10)


def turn_clockwise():
    pen1.right(10)


def clear_screen():
    pen1.reset()


heading()

screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=turn_anti_clockwise)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
