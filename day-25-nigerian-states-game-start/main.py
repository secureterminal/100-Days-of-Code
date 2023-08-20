import turtle
import pandas as pd
from helper_functions import add_state_to_map

all_states = {
    'states': [],
    'x': [],
    'y': []
}
guessed_states = []
states_df = pd.DataFrame(all_states)


# Function to print the coordinates when the screen is clicked
def print_coordinates(x, y):
    global states_df
    my_text = turtle.textinput("Text Input", "Enter your text:")

    # New row data
    new_row = {'States': my_text, 'x': x, 'y': y}

    # Add the new row using loc
    states_df = states_df.append(new_row, ignore_index=True)
    print(f"Mouse clicked at coordinates: ({my_text}, {x}, {y})")
    print(states_df)


# Get user input using textinput
check_states = turtle.textinput("User Input", "Have you inserted states coordinates (Y/N): ")

screen = turtle.Screen()


image = "nigeria_blank.gif"
screen.addshape(image)
turtle.shape(image)

if check_states.lower() == "n":
    # Register the click event handler
    turtle.onscreenclick(print_coordinates)
else:
    states_df = pd.read_csv("37_nigerian_states.csv")
    # print(states_df)

is_this_guessed = False

# Check if we still have states in the data frame
while len(states_df) != 0:
    total_guessed = len(guessed_states)
    screen.title(f"Nigerian States Game, {total_guessed}/37 states guessed")

    if len(guessed_states) == 0:
        states_question = "What's your first state's name?, type 'X' to exit"
    else:
        states_question = "What's another state's name?, type 'X' to exit"

    if is_this_guessed:
        states_question = "This have been guessed, please guess another state's name, , type 'X' to exit"

    # Display question
    answer_state = screen.textinput(title=f"{total_guessed}/37 states guessed", prompt=states_question).strip().title()
    states_question = "What's another state's name?, type 'X' to exit"
    is_this_guessed = False

    # Convert states series to list and check if answered state is in the list
    states_list = states_df.states.tolist()
    is_present = False
    if answer_state in states_list:
        is_present = True

    if answer_state.lower() == "x":
        print(f"You missed {len(states_df)} state(s) as shown below \n {states_list}")
        new_data = pd.DataFrame(states_list)
        new_data.to_csv("states_to_learn.csv")
        print("Exiting loop...")
        turtle.bye()
        break
    elif answer_state in guessed_states:
        # check if it has been answered
        is_this_guessed = True
        continue

    elif is_present:
        selected_columns = states_df[states_df['states'] == answer_state][['x', 'y']]
        #     remove from df
        states_df = states_df[states_df['states'] != answer_state]
        guessed_states.append(answer_state)
        # print("Selected Columns: ", selected_columns['x'], " - ", selected_columns['y'])
        print(selected_columns)
        # add_state_to_map(selected_columns['x'], selected_columns['y'], answer_state, 10)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(selected_columns.x), int(selected_columns.y))
        t.write(answer_state)
    elif not is_present:
        print("Wrong guess")

    print(answer_state, " ", len(states_df))


if len(guessed_states) == 37:
    print("SUCCESS !!!!!!!!!!!")


# Keep the window open until the user closes it
# turtle.done()

# Save location data if not done previously
if check_states.lower() == "n":
    states_df.to_csv("alt_37_nigerian_states_alt.csv")
