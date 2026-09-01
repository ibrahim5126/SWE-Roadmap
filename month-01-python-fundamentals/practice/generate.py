import random

cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
random.shuffle(cards)

for card in cards:
    print(card)