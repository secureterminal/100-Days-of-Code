# Note that this code is not to be run in the Python console. However, it should be run in Reeborgs World website.
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# or wall_in_front()    
def jump():
    count = 1
    turn_left()
    move()
    
    
    turn_right()
    while wall_in_front():
        turn_left()
        move()
        turn_right()
        count +=1
    
    move()
    turn_right()
    for r in range(count):
        move()
    
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()