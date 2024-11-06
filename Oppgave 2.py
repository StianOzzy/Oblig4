
# -----------------------   initialization     -----------------------
    # function: Create a deck of cards


    # function: Shuffle the order of the cards


# -----------------------   gameplay functions  -----------------------
    # function: deal card
        # must obtain card in player inventory or dealer inventory
        # must remove card from "cardbank" inventory

    # display hands
        # displays current hands of player and dealer (minus dealer first card)

    # check sum
        # check for blackjack or bust

# -----------------------          Game         -----------------------

    # Deal initial cards
        # two cards from "cardbank" inventory to player hand
        # two cards from "cardbank" inventory to dealer hand. Only one revealed to player

    # General gameplay loop
        # 1 check sum

        # 2 ask hit or stand
            # if hit
            # -> deal card from "cardbank" inventory to player hand
            # check sum