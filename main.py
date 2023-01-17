import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("TURTLE RACING")
screen.tracer(0)
screen.setup(width=600, height=600)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    if player.end_line():
        player.goto_start()
        score.increase_level()

    for c in car.all_cars:
        if c.distance(player) < 25:
            score.game_over()
            game_is_on = False

screen.exitonclick()
