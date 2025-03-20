from turtle import Screen
from game_resources.walls import Walls
from game_resources.paddle import Paddle
from game_resources.ball import Ball
from game_resources.block import Block


# Screen
screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Breakout game")
screen.tracer(0) # 1 TEST

# Walls
walls = Walls()
walls.print_walls()

# Paddle
paddle = Paddle()

# Ball
ball = Ball()


# Blocks
screen.tracer(0) # 2 TEST
list_of_block = []
block_step = 5
line_step = 0
for line in range(6):
    for _ in range(9):
        block = Block()
        block.color(block.colors[line])
        block.goto(-395 + block_step, 0 + line_step)
        list_of_block.append(block)
        block_step += 96
    block_step = 5
    line_step += 40


# Onkey function
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(ball.ball_move_to_start, "space" )

# Game body
screen.tracer(0)
game_is_on = True
while game_is_on:
    screen.update()
    if not ball.stand_on_start:
        ball.move()

    # Border checking and pounce xcor
    if ball.xcor() > 420 or ball.xcor() < -430:
        ball.dx *=-1

    # Border checking and pounce ycor by top
    if ball.ycor() > 350:
        ball.dy *= -1

    # Block checking
    for block in list_of_block:
        if ball.distance(block) < 40:
            pass

    # Paddle collision
    if ball.ycor() < -385 and ball.distance(paddle) < 40:
        ball.dy *= -1
