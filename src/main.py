import random

from full_deck import card_deck

def get_index_card(deck, card):
    index_card = deck.index(card)
    return index_card
    
def get_card(deck, quantity):
    random_card = random.choices(deck, k = quantity)
    random.shuffle(deck)
    
    return random_card 

def main():
    player_hand = get_card(2)
    computer_hand = get_card(2)
    
    print(player_hand)
    print(computer_hand)

    # card_indexes = []

if __name__ == "__main__":
    main()
