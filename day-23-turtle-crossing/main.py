import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Cross')
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.up, 'Up')
screen.onkeypress(player.down, 'Down')




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    if player.ycor() > 260:
        score.increase_level()
        player.go_to_start()
        car.increase_speed()

    for any_cars in car.all_cars:
        if player.distance(any_cars.position()) < 25:
            score.write_gameover()
            game_is_on = False


screen.exitonclick()




