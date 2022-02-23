from turtle import Turtle, Screen
import random

screen = Screen()
timmy = Turtle()

timmy.speed('fastest')

# Setting the screen color-mode
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


steps = 0
while steps < 90:
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(4)

    steps += 1


screen.exitonclick()
