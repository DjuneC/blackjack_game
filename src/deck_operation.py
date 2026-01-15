import random
import string

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

def calcul_score(hand):
    score = 0

    for card_value in hand:
        if card_value.startswith("A"):
            score += 11

        elif card_value in string.ascii_uppercase:
            score += 10

        else:
            score += int(card_value)

    return score