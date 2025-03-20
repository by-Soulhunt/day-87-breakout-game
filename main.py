from turtle import Screen
from game_resources.walls import Walls
from game_resources.paddle import Paddle


# Screen
screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Breakout game")
screen.tracer(0)


# Walls
walls = Walls()
walls.print_walls()


# Paddle
paddle = Paddle()


# Onkey function
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")


# Game body
game_is_on = True
while game_is_on:
    screen.update()