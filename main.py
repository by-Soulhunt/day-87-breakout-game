from turtle import Screen
from game_resources.walls import Walls
from game_resources.paddle import Paddle
from game_resources.ball import Ball


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


# Ball
ball = Ball()

# Onkey function
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(ball.ball_move_to_start, "space" )

# Game body
game_is_on = True
while game_is_on:
    screen.update()
    if not ball.stand_on_start:
        ball.move()