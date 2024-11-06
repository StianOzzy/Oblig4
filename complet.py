import random

#-----------------------------------------------------------------------------------------------------------------------

# ___ Create deck ___
def create_new_deck():
    cardbank = []
    suits = ["♠", "♥", "♦", "♣"]
    for i in range(1,14):
        for suit in suits:
            face = {1: "A", 11: "J", 12: "Q", 13: "K"}
            if i in face:
                i = face[i]
            cardbank.append((i,suit))
    return cardbank

# ___ Shuffle Functionality ___
def shuffle_deck(_cards):
    random.shuffle(_cards)

# ___ Drawing cards ___
def draw_card(to_inv, __cards):
    to_inv.append(__cards.pop())

# ___ Show hands ___
def show_player_hands(hand):
    for i in range(len(hand)):
        rank, suit = hand[i]
        if rank != 10:
            print(f"┌─────────┐\n"
                  f"│{rank}        │\n"
                  f"│         │\n"
                  f"│    {suit}    │\n"
                  f"│         │\n"
                  f"│       {rank} │\n"
                  f"└─────────┘")
        else:
            print(f"┌─────────┐\n"
                  f"│{rank}       │\n"
                  f"│         │\n"
                  f"│    {suit}    │\n"
                  f"│         │\n"
                  f"│       {rank}│\n"
                  f"└─────────┘")

# ___ Check sum ___
def check_sum(hand):
    total_sum = 0
    for i in range(len(hand)):
        rank, suit = hand[i]
        ace_amount = 0
        invface = {"A": 11, "J": 10, "Q": 10, "K": 10}
        if rank in invface:
            rank = invface[rank]
        if rank == 11:
            ace_amount += 1
        total_sum = total_sum + rank
        if total_sum > 21 and ace_amount > 0:
            total_sum -= 10
    return total_sum


# ___ Game start ___

while True:
    player_hand = []
    dealer_hand = []

    cards = create_new_deck()
    shuffle_deck(cards)

    print("Welcome to Blackjack")

    draw_card(player_hand, cards)
    draw_card(dealer_hand, cards)
    draw_card(player_hand, cards)
    draw_card(dealer_hand, cards)