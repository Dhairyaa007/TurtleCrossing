from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.clear()
        self.update()

    def update(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align=ALIGN, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
