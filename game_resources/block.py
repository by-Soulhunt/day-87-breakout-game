from turtle import Turtle


class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 4)
        self.goto(-395, 0)
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def block_creating(block_step, line_step, list_of_block):
    for line in range(6):
        for _ in range(9):
            block = Block()
            block.color(block.colors[line])
            block.goto(-395 + block_step, 0 + line_step)
            list_of_block.append(block)
            block_step += 96
        block_step = 5
        line_step += 40

def deleting_blocks(list_of_block):
    for i in list_of_block:
        i.hideturtle()
    list_of_block = []