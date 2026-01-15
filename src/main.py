import random

from full_deck import card_deck as total_deck
from deck_operation import get_card, get_index_card, remove_card_from_deck, calcul_score

def main():
    random.shuffle(total_deck)
    decision = True

    player_hand = get_card(total_deck, 2)
    computer_hand = get_card(total_deck, 2)

    remove_card_from_deck(total_deck, player_hand)
    remove_card_from_deck(total_deck, computer_hand)

    while decision:

        decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

        if not decision in ['y', 'n']:
            print("You need a pair of glasses, look at the menu again.")
            continue

        if decision == 'n':
            decision = False

        player_score = calcul_score(player_hand)
        computer_score = calcul_score(computer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

if __name__ == "__main__":
    main()
