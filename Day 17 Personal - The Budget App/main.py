from budget import Budget

name = input('Please input your name: ').title()
my_Budget = Budget(name)

start_budget = True

while start_budget:
    choice = input(f'''
            Hello {name}, what would you like to do today? Please choose from below:
            1: To create a new budget category, press 1
            2: To perform a budget operation (Withdraw/Deposit), press 2
            3: To check balance, press 3
            4: To transfer balance between categories, press 4
            Press any other key to exit...
        ''')
    if choice == '1':
        my_Budget.add_category()
        print(f'\n{name}, please see below list of your budget categories and balances\n')
        count = 1
        for budget in my_Budget.categories:
            print(f'Budget No. {count}')
            print(f'Name: {budget}')
            print(f'Description: {my_Budget.categories[budget][1]}')
            print(f'Balance: ₦{my_Budget.categories[budget][2]:,.2f}\n')
            count += 1

    elif choice == '2':
        operation = input('Please choose "w" for Withdrawal or "d" for deposit: ').lower()
        if operation == 'w':
            my_Budget.withdraw()
            continue
        elif operation == 'd':
            my_Budget.deposit()
            continue
        else:
            print(f'Wrong choice, Thanks for your patronage {name}, hope to see you soon...\n')
            start_budget = False
            continue

    elif choice == '3':
        my_Budget.check_balance()
        continue

    elif choice == '4':
        my_Budget.transfer_balance()
        continue
    else:
        print(f'Thanks for your patronage {name}, hope to see you soon...\n')
        start_budget = False
        continue


