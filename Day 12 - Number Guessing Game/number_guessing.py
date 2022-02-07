from art import logo
import random
print(logo)



print('Welcome to the number guessing game\n')

print('I am thinking of a number between 1 and 100\n')

level = input('Choose a difficulty level, type "easy" or "hard" >>>   ').lower()

if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5
else:
    attempts = 0

guess = random.randint(1, 100)

win_status = False

while attempts > 0:
    print(f'You have {attempts} attempts remaining to guess the number. ')

    user_guess = input('Make a guess:  ')

    try:
        user_guess = int(user_guess)

        if user_guess > guess:
            print('Guess is too high\n')
            attempts -= 1
        elif user_guess < guess:
            attempts -= 1
            print('Guess is too low \n')
        else:
            print(f'Congratulations, you guesed right, the number is {guess} \n')
            win_status = True
            break
        

    except Exception as e:
        print(e)

if attempts < 0 and win_status == False:
    print('Sorry you have 0 attempts left, you lose')