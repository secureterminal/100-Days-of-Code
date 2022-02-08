import art
import os
from random import randint
from game_data import data as dt

logo = art.logo
vs = art.vs




def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def compare(person1, person2):
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']} \n")

    print(vs)

    print(f"\nCompare B: {person2['name']}, a {person2['description']}, from {person2['country']} \n")
    
    return input('Who has more followers? A or B>>> \t').lower()

 

def choose_person(person_list):
    '''Returns the index of the chose person'''
    return randint(0, len(person_list) - 1)


def game():
    count = 0
    guess_remaining = len(dt)
    winning_streak = True
    while winning_streak and guess_remaining > 0:
        count += 1
        clearConsole()
        print(logo)
        if count > 1:
            print(f'You are right! Current Score: {count-1}')
        

        if count == 1:
            person1_index = choose_person(dt)
            person_one = dt[person1_index]
            del dt[person1_index]
        else:
            person1_index = winner_index
            person_one = higher_follower
        
        person2_index = choose_person(dt)
        person_two = dt[person2_index]
        del dt[person2_index]

        print(f'\n{len(dt)} people left ')

        # print(person1_index, person2_index)

        user_choice = compare(person_one, person_two)

        if person_one['follower_count'] > person_two['follower_count']:
            higher_follower = person_one
        else:
            higher_follower = person_two

        if user_choice == 'a':
            if person_one == higher_follower:
                winner_index = person1_index
            else:
                print(f'\nWrong input, Sorry you lost, you finished the game with {count-1} point(s)\n')
                winning_streak = False
        elif user_choice == 'b':
            if person_two == higher_follower:
                winner_index = person2_index
            else:
                print(f'\nWrong input, Sorry you lost, you finished the game with {count-1} point(s)\n')
                winning_streak = False
        else:
            # print('Wrong input, you lost')
            print(f'\nWrong input, Sorry you lost, you finished the game with {count-1} point(s)\n')
            winning_streak = False
        
        guess_remaining = len(dt)

    if guess_remaining == 0 and winning_streak == True:
        print(f'\nCongratulations, you finished the game with {count} point(s)\n')
        




        
game()