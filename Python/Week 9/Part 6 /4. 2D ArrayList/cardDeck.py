from random import shuffle

suits = ["♥", "♦", "♣", "♠" ]
deck =[]
for item in suits:
    for card in range(1,14):
        if card == 11:
            deck.append("J" + item)
        elif card == 12:
            deck.append("Q" + item)
        elif card == 13:
            deck.append("K" + item)
        elif card == 1:
            deck.append("A" + item)
        else:
            deck.append(str(card) + item)
print(deck)

shuffle(deck)

print(deck)


# deal five hand  ?