# Oppgave 2

import os

def clear_console() -> None:
    os.system('clear' if os.name == 'posix' else 'cls')


# Cards index

class Cards:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def get_info(self):
        return f"{self.type}, {self.value}"


def print_card(self):
    return f" _____ \n|{self.type}    |\n|  {self.value}  |\n|     |\n|____{self.type}|\n"


card1 = Cards("♠", 1)
card2 = Cards("♥", 2)

print(print_card(card1))
print(print_card(card2))