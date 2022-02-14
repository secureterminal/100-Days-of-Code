from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

menu = Menu()
coffee_maker.report()
money_machine.report()

coffee_machine_is_on = True

while coffee_machine_is_on:
    choices = menu.get_items()
    user_order = input(f'Please choose a coffee: ({choices})>>> ')

    if user_order == 'off':
        coffee_machine_is_on = False

    elif user_order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


