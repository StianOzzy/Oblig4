# Oppgave 2

# Cards index

class Cards:
    def __init__(self, type, value, index):
        self.type = type
        self.value = value
        self.index = index
    
    def get_info(self):
        return f"{self.type}, {self.value}, {self.index}"

    def print_card(self):
        return f"{self.type}____ \n|     |\n|  {self.value}  |\n|     |\n|____{self.type}|\n"


card1 = Cards("♠", 1, 1)
card2 = Cards("♥", 2, 2)


print(" _____ \n"
      "|     |\n"
      "|     |\n"
      "|     |\n"
      "|_____|\n")

print(print_card(card1))