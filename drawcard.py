import random

# Create deck

cardbank = []
suits = ["♠", "♥", "♦", "♣"]
for i in range(1,14):
    for suit in suits:
        cardbank.append((i,suit))

print(cardbank)
print(len(cardbank))


def shuffle_deck():
    random.shuffle(cardbank)
    print(cardbank)
    print(len(cardbank))
shuffle_deck()

def draw_card(to_inv):
    to_inv.append(cardbank.pop())

player_hand = []

draw_card(player_hand)
print("cards in bank:", len(cardbank))
print("player hand:", player_hand)

