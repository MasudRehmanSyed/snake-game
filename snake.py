import time
from turtle import Turtle
import random as rd

MOVE_DISTANCE = 20
STARTING_COORDINATES = [(x, 0) for x in range(0, -60, -20)]
WIDTH = 290
HEIGHT = 290
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
            self.segments.append(new_segment)

    def extend(self):
        extended_segment = Turtle("square")
        extended_segment.color('white')
        extended_segment.pu()
        new_position = self.segments[-1].pos()
        extended_segment.goto(new_position)
        self.segments.append(extended_segment)

    def move(self):
        """ moves forward by going to the position of square ahead"""

        for i in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[i - 1].pos()
            self.segments[i].goto(new_position)

        # if not(-abs(WIDTH) < self.head.xcor() < WIDTH):
        #     self.head.undo()
        #     self.head.setheading(rd.choice(DIRECTION) - self.head.heading())
        # elif not (-abs(WIDTH) < self.head.ycor() < WIDTH):
        # #     self.head.undo()
        # #     self.head.setheading(rd.choice(DIRECTION) - self.head.heading())

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

        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def wall_collision(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if -280 > x or x > 280 or -280 > y or y > 280:
            print('hit wall')
            return False
        return True

    def tail_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return False
        return True
