from turtle import Turtle, Screen
import random
screen = Screen()
timmy = Turtle()
timmy.home()
timmy.shape("turtle")
timmy.speed('fastest')
timmy.width(10)
# Setting the screen color-mode
screen.colormode(255)
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'cyan', 'black', 'magenta', 'orange', 'indigo', 'lightblue']
direction = ['left', 'right']
angle = [90, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


steps = 0
while steps < 1000:
    timmy.color(random_color())
    timmy.fd(50)
    timmy.right(random.choice(angle))

    steps += 1


screen.exitonclick()
