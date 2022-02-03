from art import logo
import os 

print(logo)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b






def do_math(a, b):
    if operator == '+':
        x = add(a, b)
    elif operator == '-':
        x = subtract(a, b)
    elif operator == '*':
        x = multiply(a, b)
    elif operator == '/':
        x = divide(a, b)
    else:
        x = None
        final = f'The operator "{operator}" is invalid '
        return final, x

    final = f'{a} {operator} {b} = {x}'
    return final, x


try:
    first = int(input('What is the first number: '))
    continue_operation = True

    repeat = False

    
    while continue_operation:
        if repeat: print(f'Previous result is {answer} ')
        print('+\n-\n*\n/\n')
        operator = input('Pick an operator from the above: ')
        next = int(input('What is the next number: '))
        
        if repeat == False:
            sentence, answer = do_math(float(first), float(next))
            print(sentence)
            if sentence == f'The operator "{operator}" is invalid ': break
            repeat = True
        else:
            sentence, answer = do_math(float(answer), float(next))
            print(sentence)
            if sentence == f'The operator "{operator}" is invalid ': break
            

        user_continue = input('Do you want to continue the operation? "Y for YES", "S to start afresh", or "any other key for NO" >>> ').lower()

        if user_continue == 'y':
            continue
            clearConsole()
        elif user_continue == 's':
            repeat = False
            clearConsole()
            first = int(input('What is the first number: '))
        else:
            print('Thanks for using the calculator app\n\n')
            continue_operation = False
except:
    print('User error!!! Wrong data entered')
        
    