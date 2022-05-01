############### Blackjack Project #####################

import random
from replit import clear
from logo import logo

#start the game
end_game = False
while not end_game:
    clear()
    print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    #deal, 2 card for player and 2(1 hidden for computer)
    # user_cards, comp_cards = [] , []

    def deal_cards(deal_hand = [], deals = 2):
        for _ in range(deals):
            hand = random.choice(cards)
            deal_hand.append(hand)
        return deal_hand

    user_cards = deal_cards(deals = 2)
    comp_cards = deal_cards(deals = 2)
    user_cards, comp_cards = [11, 10], [11, 10] # forcing value for testing

    # comp_hand = random.choices(cards, k=2)
    print(user_cards, comp_cards)
    print(user_cards, [comp_cards[0], '*'])


    # add up user and computer scores
    def calculate_score(arr):
        total = sum(arr)
        if (len(arr) == 2) and (total == 21):
            return 0
        if (total > 21) and (11 in arr):
            # arr = [1 if x == 1 else x for x in arr]
            for idx, num in enumerate(arr):
                if num == 11:
                    arr[idx] = 1
        compare()
        return sum(arr)

    user_sum = sum(user_cards)
    comp_sum = sum(comp_cards)
    print(user_sum, comp_sum)

    # Does user or computer has black jack (21). 

    def compare(user_cards, comp_cards):
        if calculate_score(user_cards) == 21 and calculate_score(comp_cards) == 21:
            # print(f"cal score is {calculate_score(user_cards)} and {calculate_score(comp_cards)}")
            print("Draw!!!")
            end_game = True

        if calculate_score(user_cards) == 0:
            print("You win!!!")
        elif calculate_score(user_cards) > 21:
            print("You lose!!!")

        if calculate_score(comp_cards) == 0:
            print("Computer wins!!!")
        elif calculate_score(comp_cards) > 21:
            print("Computer wins!!!")


    #another card?
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while user_choice == 'y':
        deal_cards(user_cards, 1)
        calculate_score(user_cards)
        while(comp_sum < 17):
            deal_cards(comp_cards, 1)
            calculate_score(comp_cards)

    #another game?
    another_game = input("Do you want to play anothe game (y/n)?").lower()
    if another_game == 'n':
        end_game = True


    



