import random
import sys

from logo import art
from full_deck import card_deck as deck
from deck_operation import handle_hand_value, handle_deal_card


def main():
    random.shuffle(deck)

    player_hand = [deck[0], deck[1]]
    dealer_hand = [deck[0], deck[1]]

    player = handle_hand_value(player_hand)
    dealer = handle_hand_value(player_hand)

    decision = input("Do you want to play a game of Blackjack ♠️♥️♦️♣️? Type 'y' or 'n'\n--> ").lower()

    if decision == 'y':
        print(logo)
    elif decision == 'n':
        sys.exit()
    else:
        print("Wrong input ❌")
        main()

    while True:
        display_hand(player_hand, dealer_hand, player, dealer, hide_dealer_hand=False)

        if player['value'] > 21:
            print("Burst, dealer win.")
            return

        choice = input("Do you want to hit or stand, h/s?\n--> ")

        if choice == 'h':
            handle_deal_card(deck=deck, hand=player_hand)
            player = handle_hand_value(player_hand)
        elif choice == 's':
            break

    while dealer['value'] < 17:
        handle_deal_card(deck=deck, hand=dealer_hand)
        dealer = handle_hand_value(dealer_hand)

    display_hand(player_hand, dealer_hand, player, dealer, hide_dealer_hand=True)

    handle_winner(player, dealer)
    

if __name__ == "__main__":
    main()
