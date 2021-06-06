from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()

        self.pu()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed(0)
        self.goto(randint(-280, 280), randint(-280, 280))
        self.new_food()

    def new_food(self):
        self.goto(randint(-280, 280), randint(-280, 280))
