# imports
import random
import time

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
    print(hand)
    """
    for i in range(len(hand)):
        rank, suit = hand[i]
        if rank != 10:
            print(f"┌─────┐\n"
                  f"│{rank}    │\n"
                  f"│  {suit}  │\n"
                  f"│   {rank} │\n"
                  f"└─────┘")
        else:
            print(f"┌─────┐\n"
                  f"│{rank}   │\n"
                  f"│  {suit}  │\n"
                  f"│   {rank}│\n"
                  f"└─────┘")
    """

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

# ___ Placing bet ___
def place_bet():
    global chips
    while True:
        if chips == 1:
            print("You currently have 1 chip.")
        else:
            print(f"You currently have {chips} chips.")

        global bet_amount
        bet_amount = int(input("How many chips do you want to bet?\n\n>"))

        if bet_amount > chips:
            print("You do not have enough chips for that bet. Try again.")
        elif bet_amount <= 0:
            print("Invalid bet amount. Try again.")
        elif bet_amount >= 0 and bet_amount <= chips:
            chips -= bet_amount
            break

    # ___ Game start ___

# ___ Game initializer ___
def start_game():


while True:

    player_hand = []
    dealer_hand = []
    chips = 10

    cards = create_new_deck()
    shuffle_deck(cards)

    print("Welcome to Blackjack")

    place_bet()
    print(f"\nYou placed a bet of {bet_amount} chips")
    print("Shuffling...\n")
    time.sleep(1)
    draw_card(player_hand, cards)
    draw_card(dealer_hand, cards)
    draw_card(player_hand, cards)
    draw_card(dealer_hand, cards)
    show_player_hands(f"Players hand:\n{player_hand}\n")
    show_player_hands(f"Dealers hand:\n{dealer_hand[1]}, (UNKNOWN)\n")
    draw_card(dealer_hand, cards)
    show_player_hands(f"Dealers hand:\n{dealer_hand[1]}, (UNKNOWN)\n")
    break