
from turtle import Turtle
ALIGNMENT = 'center'
FONTS = ('Ariel', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_score()
        self.color('white')
        self.penup()
        self.goto(0, 390)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score - {self.score}", move= False, align= ALIGNMENT, font= FONTS)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER!!!", move= False, align= ALIGNMENT, font= FONTS)
        # print('You lose!!!')
        





