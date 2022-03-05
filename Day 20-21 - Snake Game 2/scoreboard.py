from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=("Arial", 20, "normal"))

    # def game_over(self):
    #     self.color('red')
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align='center', font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=("Arial", 20, "normal"))
        # self.goto(0, 0)
