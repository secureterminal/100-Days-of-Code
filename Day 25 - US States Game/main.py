import turtle
import pandas as pd
from game_logic import GameLogic
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
game = GameLogic()
# scores = Scoreboard()
# print(answer)
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

start_game = game.check_remaining_states()
while start_game:
    answer = screen.textinput(title=f'{game.score.score}/50', prompt='Whats the state\'s name?').strip()
    game.check_option(answer)

    if game.check_option(answer) == 'None':
        print(game.check_option(answer))
    else:
        print(answer)
        # scores.increase_score()

    if answer.lower() == 'stop':
        start_game = False
    else:
        start_game = game.check_remaining_states()

df = pd.DataFrame(game.state_list)
df.to_csv("states_to_learn.csv")

# screen.exitonclick()
