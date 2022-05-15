
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid =  1, stretch_len = 1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_y(self):
        # print('hitting the wall')
        self.y_move *= -1 
        self.move_speed *= 0.9
        
    def bounce_ball_x(self):
        # print('hitting the wall')
        self.x_move *= -1 
        self.move_speed *= 0.9

    
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_ball_x()
        self.move_speed = 0.1



