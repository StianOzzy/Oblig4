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