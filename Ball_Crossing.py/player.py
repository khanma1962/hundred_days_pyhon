
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        # self.shape('ball.gif')
        self.setheading(90)
        self.color('white')
        self.penup()
        self.goto(STARTING_POSITION)
        self.SPEED = MOVE_DISTANCE

    def go_up(self):
        new_y = self.ycor() + self.SPEED
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.SPEED
        self.goto(self.xcor(), new_y)

    def reset_player(self):
        # self.reset()
        self.goto(STARTING_POSITION)

    def is_cross_finish(self):
        if self.ycor() == 280:
            return True
        else:
            return False




    