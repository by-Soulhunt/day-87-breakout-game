from turtle import Turtle


class Walls(Turtle):
    """
    Game walls - Left, Top, Right
    """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.pencolor("white")
        self.penup()
        self.pensize(10)
        self.setheading(90)
        self.goto(-445, -440)


    def print_walls(self):
        """
        Print walls
        :return:
        """
        self.pendown()
        self.forward(800)
        self.right(90)
        self.forward(882)
        self.right(90)
        self.forward(800)
        self.hideturtle()