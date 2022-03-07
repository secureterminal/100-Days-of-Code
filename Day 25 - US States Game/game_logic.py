from turtle import Turtle
import pandas as pd
from scoreboard import Scoreboard


class GameLogic(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.us_data = pd.read_csv('50_states.csv')
        self.state_df = self.us_data['state']
        # print(f'ALL States: {self.state_df}')
        self.state_list = self.us_data.state.to_list()
        self.score = Scoreboard()
        # print(self.state_list)

    def check_option(self, answer):
        if answer.title() in self.state_list:
            x = self.us_data[self.us_data['state'] == answer.title()].iloc[0]['x']
            y = self.us_data[self.us_data['state'] == answer.title()].iloc[0]['y']
            # self.state_list.pop(answer)
            # print(self.state_list)
            self.state_list.remove(answer.title())
            print(x, y)
            # print(type(x))
            self.hideturtle()
            self.penup()
            self.goto(x, y)
            self.pendown()
            self.score.increase_score()
            self.write(f'{answer.title()}', align='center', font=("Arial", 6, "normal"))
            return x
        else:
            return 'None'

    def check_remaining_states(self):
        if len(self.state_list) == 0:
            return False
        else:
            return True

