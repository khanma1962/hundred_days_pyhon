
from turtle import Turtle

ALIGNMENT = 'center'
FONTS = ('Ariel', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Score : {self.score_l}", align= ALIGNMENT, font= FONTS)
        self.goto(100, 250)
        self.write(f"Score : {self.score_r}", align= ALIGNMENT, font= FONTS)

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_score()

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_score()


    def game_over(self):
        pass


    

