
from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.color('white')
        self.penup()
        self.goto(0, 250)
        # self.update_level()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Level : {self.level}", align= 'center', font= FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()
        self.goto(0, 250)

    def collision(self):
        self.goto(0,0)
        # while True:
        #     # time.sleep(1)
        self.clear()
        self.write(f"You lost!!!", align= 'center', font= ("Courier", 48, "normal"))
            # time.sleep(1)
            # self.write(f" ", align= 'center', font= ("Courier", 48, "normal"))

    def game_won(self):
        self.clear()
        self.update_score()
        self.goto(0,0)
        self.write(f"You won!!!", align= 'center', font= ("Courier", 48, "normal"))




