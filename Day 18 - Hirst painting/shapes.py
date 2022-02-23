from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color('red')
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'cyan', 'black', 'magenta', 'orange', 'indigo', 'lightblue']

sides = 3
for a in range(10):
    for b in range(sides):
        timmy.color(colors[sides-3])
        timmy.fd(100)
        timmy.right(360/sides)

    sides += 1

screen = Screen()
screen.exitonclick()