

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

WIDTH = 1000
HEIGHT = 1000

# create snake body
screen = Screen()
screen.setup(width = WIDTH, height = HEIGHT )
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()
 
    # detect collision with food
    if snake.head.distance(food ) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # detect collision with the wall
    if not((-0.5*WIDTH) < snake.head.xcor() < (0.5*WIDTH) and (-0.5*HEIGHT) < snake.head.ycor() < (0.5*HEIGHT)):
        score_board.game_over()
        game_is_on = False

    # detect collision with the tail
    #if the tail collides with any segment, trigger game over sequence
    # for segment in snake.segments[4:]:
    #     if snake.head.distance(segment) < 10:
    #         print('head touching')
    #         score_board.game_over()
    #         game_is_on = False



screen.exitonclick()

