from turtle import Turtle, Screen

mez = Turtle()
screen = Screen()


def move_forwards():
    mez.forward(100)


def move_backwards():
    mez.back(100)


def turn_left():
    mez_heading = mez.heading() + 10
    mez.setheading(mez_heading)
    # mez.forward(100)


def turn_right():
    mez.rt(10)


def clear():
    mez.clear()
    mez.penup()
    mez.home()
    mez.pendown()


screen.listen()
# Remember to remove the braces from inner functions when running higher order functions
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")


screen.exitonclick()
