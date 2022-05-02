# Coffee Machine

# from coffee_machine.data import MONEY
from data import RESOURCES, MENU, MONEY

# parameters
is_on = True
profit = 0

#process coins


#is_sufficient_resource?

#print report

#is_transaction_successful?



print("Welcome to the Coffee Machine!!!")
choice = input("What would you like?  Espresso(e)/Latte(l)/Cappuccino(c) : ").lower()

def transactions(choice):
    if choice == 'report':
        print(f"The resources are {RESOURCES}")
    else:
        if(choice != 'e') or (choice != 'l') or (choice != c):
            print("Please insert coins.")
            q = int(input("How many quarters ? "))
            d = int(input("How many dimes ? "))
            n = int(input("How many nickles ? "))
            p = int(input("How many pennies ? "))

            coins_received = MONEY["quarter"] * q + MONEY["dime"] * d + \
                            MONEY["nickle"] * n + MONEY["pennies"] * p

            print(f"Total amount received is ${coins_received}")
        else:
            print("Please enter the correct option.")

    if(choice == 'e'):
        if MENU["espresso"]["ingredients"]["water"] < RESOURCES["water"] \
            or MENU["espresso"]["ingredients"]["coffee"] - RESOURCES["water"]:
            print("Insuffient resource!!")

        RESOURCES["water"] -= MENU["espresso"]["ingredients"]["water"]
        RESOURCES["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        coins_return = coins_received - MENU["espresso"]["cost"]
        print(f"Here is ${coins_return} in change. ")

    elif(choice == 'l'):
        RESOURCES["water"] -= MENU["latte"]["ingredients"]["water"]
        RESOURCES["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        RESOURCES["milk"] -= MENU["latte"]["ingredients"]["milk"]
        coins_return = coins_received - MENU["latte"]["cost"]
        print(f"Here is ${coins_return} in change. ")
        
    elif(choice == 'c'):
        RESOURCES["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        RESOURCES["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        RESOURCES["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        coins_return = coins_received - MENU["cappuccino"]["cost"]
        print(f"Here is ${coins_return} in change. ")

           

    print(RESOURCES)

transactions(choice)




