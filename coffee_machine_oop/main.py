
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True


#main function
while is_on:
    choice = ''
    options = menu.get_items()
    # print(f"options are {options}")
    print("Welcome to the Coffee Machine!!!")
    # while not (choice == 'off' or choice == 'report' or choice == 'espresso' or choice == 'latte' or choice == 'cappuccino'):
    choice = input(f"What would you like {options}? : ").lower()

    #off 
    if choice == 'off':
        is_on = False

    #report
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    
    #normal transaction
    else:
        drink = menu.find_drink(choice)
        print(f"drink is type {attr(drink)}")
        print(f"drink is {drink.name}, {drink.cost}")
        
        if coffee_maker.is_resource_sufficient(drink) \
                 and money_machine.make_payment(drink.cost):
                 coffee_maker.make_coffee(drink)

