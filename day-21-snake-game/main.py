from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.title('SnakeGame')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun=snake.left)


game_on = True

while game_on:
    screen.update()
    time.sleep(0.075)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset()
        snake.reset()

    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 5:
            score.reset()
            snake.reset()



screen.exitonclick()