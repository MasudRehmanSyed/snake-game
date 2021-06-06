from turtle import Turtle, Screen
import time, random
from snake import Snake

# turtle keys leftarrow uparrow rightarrow downarrow

# DECLARATIONS and STARTING VALUES
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
delay = 0.1
high_score, score = 0, 0
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

angles = [90, 180, 270]


def clean():
    screen.update()
    time.sleep(delay)


game_on = True

while game_on:
    clean()
    snake.move()


screen.exitonclick()
