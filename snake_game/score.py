
from turtle import Turtle
ALIGNMENT = 'center'
FONTS = ('Ariel', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.update_score()
        self.color('white')
        self.penup()
        self.goto(0, 390)
        self.update_score()
        self.hideturtle()
        # self.open_highest_score()

    # def open_highest_score(self):
    #     with open("data.txt") as file:
    #         self.high_score = int(file.read())
    #     print(f"On opening highest score is {self.high_score}")

    def update_score(self):
        self.clear()
        self.write(f"Score - {self.score}      High Score - {self.high_score}", move= False, align= ALIGNMENT, font= FONTS)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write("GAME OVER!!!", move= False, align= ALIGNMENT, font= FONTS)
    #     # print('You lose!!!')
        
    def reset(self):
        if self.score > self. high_score:
            self.high_score = self.score
            with open("snake_game/data.txt", mode= 'w') as file:
                file.write(str(f"{self.high_score}"))

        self.score = 0 # reset the score to zero after reset
        self.update_score()
            
        # print(f"On closing highest score is {self.high_score}")




