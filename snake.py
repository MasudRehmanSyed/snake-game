from turtle import Turtle
import random as rd

MOVE_DISTANCE = 20
STARTING_COORDINATES = [(x, 0) for x in range(0, -60, -20)]
WIDTH = 300 -10
HEIGHT = 300 -10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DIRECTION = [RIGHT, UP, LEFT, DOWN]


class Snake:
    """ This creates 3 turtle objects snake with white
    squares and moves"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_COORDINATES:
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.pu()
            new_segment.goto(i)
            new_segment.penup()
            self.segments.append(new_segment)

    def move(self):
        """ moves forward by going to the position of square ahead"""

        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i - 1].pos()
            self.segments[i].goto(self.segments[i - 1].pos())
        if not -abs(WIDTH) < self.head.xcor() < WIDTH:
            self.head.undo()
            self.head.setheading(rd.choice(DIRECTION) - self.head.heading())
        elif not -abs(WIDTH) < self.head.ycor() < WIDTH:
            self.head.undo()
            self.head.setheading(rd.choice(DIRECTION) - self.head.heading())

        self.head.forward(MOVE_DISTANCE)

    def left(self):
        """ moves the first square only, the others will follow via move_forward()"""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        # if self.head.heading() == 90:
        #     self.head.right(90)
        # elif self.head.heading() == 270:
        #     self.head.left(90)
        # elif self.head.heading() == 180:
        #     self.head.left(180)
        # else:
        #     self.head.seth(0)
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
