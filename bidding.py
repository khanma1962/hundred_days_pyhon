# bidding program

from replit import clear
#HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
more_players = True
bid_dict = {}
highest_bidder, highest_bid = '', 0

print(logo)
print("\nWelcome to the secrete auction program!!!")
while(more_players):
    name = input("What is your name?  ") 
    bid_amount= int(input("What is your bid amount in dollars? $"))
    bid_dict[name] = bid_amount
    others = input("Are there any other bidder (Y/N)? ").lower()
    if others == 'n':
        more_players = False
    else:
        clear()
clear()
print(bid_dict)

for k, v in bid_dict.items():
    if v > highest_bid:
        highest_bid = v
        highest_bidder = k

print(f"The winner is {highest_bidder} with a bid of {highest_bid}.")


