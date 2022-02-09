from coffee_machine_data import resources, MENU


def check_resources(order):
    not_enough = []
    for key in MENU[order]['ingredients']:
        if MENU[order]['ingredients'][key] > resources[key]:
            not_enough.append(key)
    if len(not_enough) > 0:
        count = len(not_enough)

        if count > 1:
            return_str = f'Sorry there is not enough'
            for ingredient in not_enough:
                return_str += f' and {ingredient}'
            return_str = return_str.replace(' and', '', 1)
            print(return_str)
            return False
        else:
            print(f'Sorry there is not enough {not_enough[0]}')
            return False
    else:
        return True


def process_coins():
    try:
        quarters = int(input('How many quarters? '))
        dimes = int(input('How many dimes? '))
        nickles = int(input('How many nickles? '))
        pennies = int(input('How many pennies? '))
        return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    except Exception as e:
        print(e)


def remove_resources(order):
    for key in MENU[order]['ingredients']:
        resources[key] -= MENU[order]['ingredients'][key]


def order_coffee():
    coffee_machine = 'on'
    money = 0
    while coffee_machine == 'on':
        coffee_choice = input("What would you like? (espresso/latte/cappuccino)>>>:  ").lower()
        if coffee_choice == 'off':
            coffee_machine = 'off'
            print("Turning off Coffee Machine")
            continue
        elif coffee_choice == 'report':
            # coffee_machine = 'off'
            print("Kindly find below reports for the Coffee Machine")
            print(f'''
                Water: {resources["water"]}ml
                Milk: {resources["milk"]}ml
                Coffee: {resources["coffee"]}g
                Money: ${money}
            ''')
            continue
        elif coffee_choice == 'espresso' or coffee_choice == 'latte' or coffee_choice == 'cappuccino':
            if check_resources(coffee_choice):
                amount_paid = process_coins()
                cost = MENU[coffee_choice]['cost']
                if amount_paid >= cost:
                    remove_resources(coffee_choice)
                    change = round(amount_paid - cost, 2)
                    print(f'Here is ${change} in change')
                    print(f'Here is your {coffee_choice} ☕, enjoy')

                    money += cost
                else:
                    print(f"Sorry that's not enough money. ${amount_paid} refunded.")
            else:
                coffee_machine = 'off'
        else:
            print('Wrong input!')
            coffee_machine = 'off'
        continue


if __name__ == "__main__":
    order_coffee()
