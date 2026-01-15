import random

from full_deck import card_deck as total_deck
from deck_operation import get_card, get_index_card, remove_card_from_deck

def main():
    random.shuffle(total_deck)

    player_hand = get_card(total_deck, 2)
    computer_hand = get_card(total_deck, 2)

    remove_card_from_deck(total_deck, player_hand)
    remove_card_from_deck(total_deck, computer_hand)

if __name__ == "__main__":
    main()
