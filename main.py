from turtle import Screen
from game_resources.walls import Walls
from game_resources.paddle import Paddle
from game_resources.ball import Ball
from game_resources.block import Block, block_creating, deleting_blocks


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
block_creating(block_step, line_step, list_of_block)


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
            ball.dy *= -1
            block.hideturtle()
            list_of_block.remove(block)

    # Lose checking
    if ball.ycor() < -450:
        ball.lose_ball()
        deleting_blocks(list_of_block)
        block_creating(block_step, line_step, list_of_block)

    # Paddle collision
    if ball.ycor() < -385 and ball.distance(paddle) < 40:
        ball.dy *= -1
