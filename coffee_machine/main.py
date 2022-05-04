# Coffee Machine

# from coffee_machine.data import MONEY
from data import RESOURCES, MENU, MONEY

# parameters
is_on = True
profit = 0
choice = ''

#process coins
def process_coins(choice):
    # if(choice == 'espresso') or (choice == 'latte') or (choice == 'cappuccino'):
    print("Please insert coins.")
    q = int(input("How many quarters ? "))
    d = int(input("How many dimes ? "))
    n = int(input("How many nickles ? "))
    p = int(input("How many pennies ? "))

    coins_received = MONEY["quarter"] * q + MONEY["dime"] * d + \
                    MONEY["nickle"] * n + MONEY["pennies"] * p

    print(f"Total amount received is ${coins_received}")
    return coins_received
    # else:
    #     print("Please enter the correct option.") 


#is_sufficient_resource?
def check_resources(drink):
    if RESOURCES["water"] >= drink["ingredients"]["water"]   \
        and RESOURCES["milk"] >= drink["ingredients"]["milk"]   \
        and RESOURCES["coffee"] >= drink["ingredients"]["coffee"]  :
        print("Updated resources!!")
        return 1
    else:
        print("not enough resources.")
        return 0



#is_transaction_successful?
def transaction(drink, coins_received):
        RESOURCES["water"] -= drink["ingredients"]["water"]
        RESOURCES["coffee"] -= drink["ingredients"]["coffee"]
        RESOURCES["milk"] -= drink["ingredients"]["milk"]

        coins_return = coins_received - drink["cost"]
        if coins_received > 0:
            print(f"Here is ${coins_return} in change. ")
        else:
            print(f"Insufficient fund. Returning ${coins_received}")


#main function
while is_on:
    print("Welcome to the Coffee Machine!!!")
    while not (choice == 'off' or choice == 'report' or choice == 'espresso' or choice == 'latte' or choice == 'cappuccino'):
        choice = input("What would you like?  Espresso/Latte/Cappuccino : ").lower()
    # print(f"your choice is {choice}")
    # print(type(choice))

    #off 
    if choice == 'off':
        is_on = False

    #report
    elif choice == 'report':
        print(f"The resources are {RESOURCES}")

    #check for resources
    else:
        drink = MENU[choice]
        print(f"drink is {drink}")
        # RESOURCES = {
        #     "water": 0,
        #     "milk": 0,
        #     "coffee":  0,
        #     }
        if check_resources(drink) == 0:
            print("Insuffecient resouces. Sorry!!!")
            break


        # check for enough money
        coins_received = process_coins(drink)
        if coins_received < drink['cost']:
            print(f"{coins_received} is not suffecient. Returning money. ")

        #transaction
        else:
            transaction(drink, coins_received)
        
    


