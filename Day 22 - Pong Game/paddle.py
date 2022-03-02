from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_pos):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(paddle_pos)

    def r_go_up(self):
        if self.ycor() - 250 < 0:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def r_go_down(self):
        if self.ycor() + 250 > 0:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def l_go_up(self):
        if self.ycor() - 250 < 0:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def l_go_down(self):
        if self.ycor() + 250 > 0:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
