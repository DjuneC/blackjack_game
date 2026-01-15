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
