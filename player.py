from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250
score = Scoreboard()


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto_start()


    def goto_start(self):
        self.goto(0, -300)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def end_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
