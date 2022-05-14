
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len = 0.5)
        self.color('yellow')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_num_x = random.randint(-280, 280)
        rand_num_y = random.randint(-280, 280)
        # print(f"rand number is {rand_num_x} and {rand_num_y}")
        self.goto(rand_num_x, rand_num_y)


    






