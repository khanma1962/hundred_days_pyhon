
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

WIDTH, HEIGHT,  = 800, 600

screen = Screen()
screen.setup(width= WIDTH, height= HEIGHT)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
left_position, right_position =  (-1 * WIDTH / 2 + 40, 0), (WIDTH / 2 - 40, 0)

p_left  = Paddle(left_position)
p_right = Paddle(right_position)

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(p_left.go_up, "w")
screen.onkey(p_left.go_down, "s")
screen.onkey(p_right.go_up, "o") 
screen.onkey(p_right.go_down, "l")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() 
    ball.move_ball()

    # detect collision
    if not(( -0.5 * HEIGHT + 20 ) < ball.ycor() < ( 0.5 * HEIGHT - 20)) :
        ball.bounce_ball_y()
   
    # collisoin with right paddle
    if (ball.distance(p_right) < 30 and ball.xcor() > HEIGHT / 2 + 20) or \
        (ball.distance(p_left) < 30 and ball.xcor() < HEIGHT / 2 + 20):
        ball.bounce_ball_x()

    # if left side is crossed
    if ball.xcor() > 380 :
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.increase_score_l()

    if ball.xcor() < -380:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.increase_score_r()
        




screen.exitonclick()

