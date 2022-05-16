
import time
from turtle import Screen
from player import Player
import player
from car_manager import CarManager
from scoreboard import Scoreboard

COLOR = 'black'

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor(COLOR)
# screen.addshape("ball.gif")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()

    #check collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score_board.collision()
            game_is_on = False
    
    #check if ball reaches other side
    if player.is_cross_finish():
        score_board.increase_level()
        car_manager.speed_up()
        player.reset_player()

    #check scoreboard
    if score_board.level == 5:
        score_board.game_won()
        time.sleep(5)
        game_is_on = False
            

screen.exitonclick()
