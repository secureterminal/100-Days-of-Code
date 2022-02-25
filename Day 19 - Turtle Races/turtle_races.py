from turtle import Turtle, Screen
import random


def start(turtle_instance, x, y, color):
    turtle_instance.color(color)
    turtle_instance.penup()
    turtle_instance.shape('turtle')
    turtle_instance.goto(x, y)


screen = Screen()
screen.setup(width=1320, height=600)
user_input = screen.textinput("Turtle Game | Bet", "Which color of turtle will win? Please enter a color").lower()
print(user_input)


def max_x_coordinate(color_list, color_dict, count_f):
    if count_f == 0:
        max_coordinate = -600
        max_color = ''
    else:
        max_coordinate = max_x
        max_color = max_x_color
    interim_max = max_coordinate
    interim_max_color = max_color
    for color in color_list:
        if color.pos()[0] > max_coordinate:
            interim_max = color.pos()[0]
            interim_max_color = color_dict[color].title()

    if interim_max_color == max_color:
        print(
            f'{interim_max_color} is still winning...\
            Old: {max_color}:{max_coordinate} New: {interim_max_color}:{interim_max} ')
    else:
        print(interim_max)
        print(
            f'{interim_max_color} is winning. \
            Old: {max_color}:{max_coordinate} New: {interim_max_color}:{interim_max}')

    return interim_max, interim_max_color


red = Turtle()
green = Turtle()
yellow = Turtle()
blue = Turtle()
purple = Turtle()
participant_list = [red, green, yellow, blue, purple]
participant_color_dict = {red: 'red', green: 'green', yellow: 'yellow', blue: 'blue', purple: 'purple'}


start(red, -590, 200, 'red')
start(green, -590, 100, 'green')
start(yellow, -590, 0, 'yellow')
start(blue, -590, -100, 'blue')
start(purple, -590, -200, 'purple')

print(red.pos()[0])
max_x = -600

count = 0
max_jump = 10
while max_x <= 580:
    red.fd(random.randint(0, max_jump))
    green.fd(random.randint(0, max_jump))
    yellow.fd(random.randint(0, max_jump))
    blue.fd(random.randint(0, max_jump))
    purple.fd(random.randint(0, max_jump))
    max_x, max_x_color = max_x_coordinate(participant_list, participant_color_dict, count)
    count += 1

print('Max X-coordinate:', max_x, 'Max Color:', max_x_color)
# check winner
if user_input.title() == max_x_color:
    print(f'Congratulations, {user_input} won!!!')
else:
    print(f'Sorry, {user_input} lost!!!, and {max_x_color} won!!!')

# print({key: rank for rank, key in enumerate(sorted(participant_color_dict, key=participant_color_dict.get,
# reverse=True), 1)})
for participant in participant_list:
    print(f'{participant_color_dict[participant].title()}: {participant.pos()[0]}')
screen.exitonclick()
