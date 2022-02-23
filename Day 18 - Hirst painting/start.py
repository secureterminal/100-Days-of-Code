from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color('red')
for a in range(720):
    timmy.fd(1)
    timmy.right(0.5)

for a in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()