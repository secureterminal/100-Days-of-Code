import all_words, stages
import random
import pickle
import time

stages = stages.stages

def greet():
    current_hour = time.strptime(time.ctime(time.time())).tm_hour

    if current_hour < 12:
        greeting = "Good Morning!"
    elif current_hour >= 12 and current_hour < 16:
        greeting = "Good AfterNoon!"
    elif current_hour >= 16:
        greeting = "Good Evening!"
    return greeting


with open('words.py', 'rb') as filehandle:
    # read the data as binary data stream
    all_word_list = pickle.load(filehandle)

    



from all_words import logo
print(len(all_word_list))

# chosen_word = word_list[random.randint(0, len(word_list)-1)]
print(logo)
random.shuffle(all_word_list) # Not necessary

user = input(f'{greet()}, Please enter your name...\t').title()
def play_game():
    
    difficulty_level = input(f'Hello {user}, Please select the lenght of words from 6 (easy mode) to 24 (legend mode)\t')
    difficulty_check = difficulty_level.isdigit()

    if difficulty_check == True:
        if int(difficulty_level) < 6 or int(difficulty_level) > 24:
            difficulty_check = False


    while not difficulty_check:
        print(f'{user}, Please input a valid number between 6 and 24')
        difficulty_level = input(f'{user} you have been asked previously to select the lenght of words from 6 (easy mode) to 24 (legend mode), please do it right\t')
        difficulty_check = difficulty_level.isdigit()

        if difficulty_check:
            if int(difficulty_level) < 6 or int(difficulty_level) > 24:
                difficulty_check = False

    word_list = []

    for word in all_word_list:
        if len(word) == int(difficulty_level):
            word_list.append(word)

    print('Difficulty', int(difficulty_level))
    print('All Word List' ,len(all_word_list))
    print('Word List' ,len(word_list)) 

    chosen_word = random.choice(word_list).lower()

    print(chosen_word)


    game_over = False
    answer = []
    guess_list = []

    for a in range(len(chosen_word)):
        answer.append("_")

    print(answer)

    lives = 6
    while not game_over and lives != 0:

        guess = input(f'\n{user}, Please guess a letter\n').lower()
        print(guess)

        if guess not in guess_list:
            guess_list.append(guess)
            count = 0
            for a in chosen_word:
                if a == guess:
                    answer[count] = a
                count+=1

            print(answer)
            if guess not in chosen_word:
                lives -= 1
                print(f'Wrong guess {user}, sorry you lose a life and you have {lives} lives left')
                print(stages[lives])
                if lives == 0:
                    print(f'Sorry {user}, you lost, the correct word is {chosen_word}')

            if '_' not in answer:
                print(f'Congratulations {user}, you have won this round, do you want to play again? choose "Y" for yes and any other key for no')
                rematch = input('>>>')
                if rematch.lower() == 'y':
                    play_game()
                else:
                    break
        else:
            print(f'{user}, you have already guessed "{guess}", please make another guess')
            
            
play_game()