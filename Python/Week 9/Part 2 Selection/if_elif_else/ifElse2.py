cardValue =input('Enter a card value: ')
suitOfCards =input('Enter a card suit: ')

# equal
if cardValue == 'King' and suitOfCards == 'Hearts':
    print('Card is a match')
else:
    print('Card is NOT a match')

# not equal
if  cardValue != 'King' and  suitOfCards != 'Hearts':
    print('Card is a match')
else:
    print('Card is NOT a match')




if not cardValue == 'King' and not suitOfCards == 'Hearts':
    print('Card is a match')
else:
    print('Card is NOT a match')




