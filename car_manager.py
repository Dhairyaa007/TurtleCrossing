from turtle import Turtle, speed
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
R_NUM = random.randint(20, 25)


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(0, 10)
        if random_chance == 1:
            car = Turtle()
            random_y = random.randint(-250, 250)
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(x=270, y=random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

