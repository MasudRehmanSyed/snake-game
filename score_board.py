from turtle import Turtle
from random import randint

ALIGNMENT = 'center'
FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)
