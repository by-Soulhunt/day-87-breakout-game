from turtle import Turtle
import random


SPEED_S = -0.35
SPEED_F = 0.35


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        angle = self.random_angle() # Generates a random float and used for choose random vector of ball
        self.dx = angle
        self.dy = abs(angle)
        self.goto(0, -380)
        self.stand_on_start = True # Ball at start position

    def move(self):
        """Getting current x and y and + random dx/dy to move"""
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)


    def lose_ball(self):  # Gets 1 or -1 to change side relatively losing ball
        """
        Return ball into start position
        """
        self.goto(0, -380)
        angle = self.random_angle()
        self.dx = angle
        self.dy = angle
        self.stand_on_start = True


    def random_angle(self):
        """Return random float value for ball angle"""
        return random.uniform(SPEED_S, SPEED_F)

    def ball_move_to_start(self):
        self.stand_on_start = False

