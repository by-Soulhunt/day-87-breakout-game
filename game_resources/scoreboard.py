from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-320, 380)
        self.color("white")
        self.current_score = 0
        self.best_score = 0


    def write_score(self):
        self.clear()
        self.write(f"Current score: {self.current_score}   |   Best Score: {self.best_score}",
                   align="left", font=("Colibri", 30, "normal"))