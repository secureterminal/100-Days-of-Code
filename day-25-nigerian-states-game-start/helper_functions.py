import turtle


def add_state_to_map(x_coord, y_coord, text, font_size=10):
    # Move the turtle to specific coordinates
    # x_coord = x
    # y_coord = y
    turtle.penup()
    print(x_coord, y_coord)
    turtle.goto(-335, -49)
    turtle.pendown()

    # Write text with a custom font size
    # font_size = 24
    # turtle.write(text, align="center", font=("Arial", font_size, "normal"))
    turtle.write(text)

