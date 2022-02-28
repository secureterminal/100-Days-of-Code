from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.score = 0
        self.color('white')
        self.write(f'Score: {self.score}', align='center', font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=("Arial", 20, "normal"))

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=("Arial", 20, "normal"))


