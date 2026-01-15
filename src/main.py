import random

from full_deck import card_deck as total_deck

def get_index_card(deck, card):
    index_card = deck.index(card)
    return index_card

def remove_card_from_deck(deck, hand):
    for card in hand:
        index_in_deck = deck.index(card)
        deck.remove(deck[index_in_deck])
    
def get_card(deck, quantity):
    random_card = random.choices(deck, k = quantity)
    
    return random_card 

def main():
    print(len(total_deck))
    random.shuffle(total_deck)

    player_hand = get_card(total_deck, 2)
    computer_hand = get_card(total_deck, 2)
    
    print(player_hand)
    print(computer_hand)

    remove_card_from_deck(total_deck, player_hand)
    remove_card_from_deck(total_deck, computer_hand)

    print("***********************************")
    
    print(len(total_deck))


if __name__ == "__main__":
    main()
