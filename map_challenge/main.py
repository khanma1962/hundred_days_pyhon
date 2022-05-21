

import pandas as pd
import numpy as np
import turtle 

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "map_challenge/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# screen.bgpic("map_challenge/us-states-game-start/blank_states_img.gif")

data = pd.read_csv("map_challenge/us-states-game-start/50_states.csv")

all_state = data['state'].to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_state)} / 50 Game State", prompt= "What is another state?")
    answer_state = answer_state.title() 
    if answer_state == 'Exit':
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        missing_data = pd.DataFrame(missing_state)
        missing_data.to_csv("map_challenge/us-states-game-start/State_to_learn.csv")
        # print(missing_state)
        break

    if answer_state in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_detail_x = int(data[data["state"] == answer_state]['x'])
        state_detail_y = int(data[data["state"] == answer_state]['y'])
        t.setposition(state_detail_x,state_detail_y)
        t.write(answer_state)
        guessed_state.append(answer_state)



# state_detail_x = int(data[data["state"] == answer_state]['x'])
# state_detail_y = int(data[data["state"] == answer_state]['y'])
# print(data[data["state"] == answer_state])
# print(state_detail_x)
# print(state_detail_y)
# turtle.setposition(state_detail_x,state_detail_y)
# turtle.write(answer_state)
# turtle.goto(int(state_detail_x), int(state_detail_y))

# def get_mouse_click(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click)

# turtle.mainloop()
# screen.exitonclick()

