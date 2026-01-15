
def handle_hand_value(hand):
    score = 0
    aces = 0

    for card_value in hand:
        if card_value.startswith('A'):
            aces += 1
            score += 11

        elif card_value in ['J', 'Q', 'K', '10']:
            score += 10

        else:
            score += int(card_value)

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    blackjack = len(hand) == 2 and score == 21
    bust = score > 21

    return {'value': score, 'blacjack': blackjack, 'bust': bust}

def handle_deal_card(deck, hand):
    card = deck.pop()
    hand.append(card)

def handle_display_hand(player_hand, dealer_hand, player, dealer, hide_dealer_hand):
    if not hide_dealer_hand:
        print(f"Your cards: {player_hand}, current score: {player['value']}")
        print(f"Computer's first card: {dealer_hand[0]}")

    else:
        print(f"Your cards: {player_hand}, current score: {player['value']}")
        print(f"Computer's first card: {dealer_hand}")

def handle_winner(player, dealer):
    if dealer['value'] > 21:
        print("Burst, player win 😎")

    elif player['blacjack'] and not dealer['blacjack']:
        print("BLACKJACK, player win 😎")
    elif not player['blacjack'] and dealer['blacjack']:
        print("BLACKJACK, dealer win 😭")
    
    elif player['value'] > dealer['value']:
        print("Player win 😎")
    elif player['value'] < dealer['value']:
        print("Dealer win 😭")

    else:
        print("Push, it's a tie ⚔️")