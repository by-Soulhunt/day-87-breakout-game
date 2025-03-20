from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 5)
        self.goto(0, -400)


    def move_right(self):
        x = self.xcor()
        if x < 372:
            x += 20
            self.setx(x)


    def move_left(self):
        x = self.xcor()
        if x > -381:
            x += -20
            self.setx(x)