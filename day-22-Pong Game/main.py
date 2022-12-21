from turtle import Turtle, Screen
from padle import Padle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.bgcolor('black')

screen.tracer(0)

r_padle = Padle((350, 0))
l_padle = Padle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(key='Up', fun=r_padle.up)
screen.onkeypress(key='Down', fun=r_padle.down)
screen.onkeypress(key='w', fun=l_padle.up)
screen.onkeypress(key='s', fun=l_padle.down)


game_on = True

while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.refresh()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_padle) < 50 and ball.xcor() > 320 or ball.distance(l_padle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        score.l_point()
        ball.reset_ball()
        speed = .1

    if ball.xcor() < -380:
        score.r_point()
        ball.reset_ball()
        speed = .1



screen.exitonclick()