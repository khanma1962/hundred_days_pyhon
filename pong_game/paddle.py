
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.COLOR = 'white'
        self.STRETCH_LEN = 5
        self.SPEED = 50

        # self.paddle = Turtle()
        self.color( self.COLOR)
        self.shape('square')
        self.shapesize(stretch_wid =  self.STRETCH_LEN, stretch_len = 0.75)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + self.SPEED
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.SPEED
        self.goto(self.xcor(), new_y)




