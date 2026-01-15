import random
import sys
import os


from art import logo
from full_deck import card_deck as deck
from deck_operation import handle_hand_value, handle_deal_card, handle_display_hand, handle_winner


def play():
    random.shuffle(deck)

    player_hand = [deck[0], deck[1]]
    dealer_hand = [deck[2], deck[3]]

    player = handle_hand_value(player_hand)
    dealer = handle_hand_value(dealer_hand)

    while True:
        handle_display_hand(player_hand, dealer_hand, player, dealer, hide_dealer_hand=False)

        if player['bust']:
            print("Bust, dealer win 😭")
            return
        elif player['value'] == 21:
            break

        choice = input("Do you want to hit or stand, h/s?\n--> ")

        if choice == 'h':
            handle_deal_card(deck=deck, hand=player_hand)
            player = handle_hand_value(player_hand)

        elif choice == 's':
            break

        print()

    while dealer['value'] < 17:
        handle_deal_card(deck=deck, hand=dealer_hand)
        dealer = handle_hand_value(dealer_hand)

    handle_display_hand(player_hand, dealer_hand, player, dealer, hide_dealer_hand=True)

    handle_winner(player, dealer)

def main():
    decision = input("Do you want to play a game of Blackjack ♠️♥️♦️♣️? Type 'y' or 'n'\n--> ").lower()

    if decision == 'y':
        print(logo)
        play()
    elif decision == 'n':
        print("Bye...")
        sys.exit()
    else:
        print("Wrong input ❌")
        main()

    input("\nPress enter to continue...")

    os.system('cls' if os.name == 'nt' else 'clear')
    main()

    

if __name__ == "__main__":
    main()
