from turtle import Turtle, Screen
import time, random
from snake import Snake
from food import Food
from score_board import ScoreBoard

# DECLARATIONS and STARTING VALUES
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
delay = 0.1


# SCORE BOARD
def pen_write(text, clear):
    pen = Turtle()
    # pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.fillcolor('red')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0)
    pen.write(f"{text}!!!", align="center", font=("Arial", 14, "bold"))

    if clear == 1:
        time.sleep(0.1)
        pen.clear()

    # pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "normal"))


# INITIALIZE ELEMENTS ON SCREEN
snake = Snake()
food = Food()
score = ScoreBoard()

# Keyboard Events
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
    # Collision with food
    if snake.head.distance(food) < 15:
        pen_write('Nom, Nom, Nom', 1)
        score.update_score()
        food.new_food()
        snake.extend()
    game_on = snake.wall_collision()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            # game_on = snake.tail_collosion()
pen_write("GAME OVER", 0)

screen.exitonclick()
