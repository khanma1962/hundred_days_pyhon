
from turtle import Screen
import time
from snake import Snake

# create snake body
screen = Screen()
screen.setup(width = 600, height = 600 )
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    # if not ((-300 < segments[0].xcor() < 300) and (-300 < segments[0].ycor() < 300)):
    #     segments[0].left(90)

# create snake food


# detect collision food



# create scoreboard


# detect collision with the wall



# detect collision with the tail



screen.exitonclick()

