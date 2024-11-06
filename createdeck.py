# Create deck

cardbank = []
suits = ["♠", "♥", "♦", "♣"]
for i in range(1,14):
    for suit in suits:
        cardbank.append((i,suit))

print(cardbank)
print(len(cardbank))