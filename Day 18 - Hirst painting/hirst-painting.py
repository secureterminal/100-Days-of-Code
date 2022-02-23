import colorgram, random
from turtle import Turtle, Screen

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 30)
all_color = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    all_color.append(tup)

print(all_color)

# The colors gotten above is filtered to remove whitish colors.
all_color = [(198, 13, 32), (250, 238, 17), (39, 76, 189), (39, 217, 69), (238, 226, 5), (229, 159, 46), (27, 40, 156),
             (215, 75, 13), (198, 15, 11), (15, 154, 15), (242, 35, 166), (229, 17, 121), (70, 10, 31), (61, 15, 8),
             (224, 141, 209), (11, 97, 62), (222, 160, 8), (51, 212, 230), (18, 19, 43), (11, 227, 239),
             (237, 156, 218), (87, 74, 209), (78, 211, 162), (84, 233, 199), (60, 233, 241), (4, 67, 41)]

mez = Turtle()
screen = Screen()
mez.hideturtle()
# Setting the screen color-mode
screen.colormode(255)
mez.penup()
mez.speed('fastest')
x = -200
y= -200


for b in range(10):
    mez.goto(x, y)
    for a in range(10):
        mez.dot(20, random.choice(all_color))
        mez.penup()
        mez.fd(50)
        mez.pendown()
        print(mez.pos())
    mez.penup()
    y += 50


screen.exitonclick()
