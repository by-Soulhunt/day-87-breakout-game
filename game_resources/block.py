from turtle import Turtle


class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 4)
        self.goto(-395, 300)
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]

