import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager:

    def __init__(self):
        self.all_cars = []
        self.start_speed = 5


    def create_car(self):

        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-250, 250))
            car.setheading(180)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.start_speed)

    def increase_speed(self):
        self.start_speed += 5













