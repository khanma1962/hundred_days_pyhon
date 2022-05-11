
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_seg_x = self.segments[seg_num - 1].xcor()
            new_seg_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_seg_x, new_seg_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != LEFT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)

