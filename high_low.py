#!/usr/bin/env python3

import random
import sys


def create_deck():
    suits = ['♡', '♢', '♤', '♧']
    ranks = range(1, 14)
    deck = [(i, j) for i in suits for j in ranks]
    random.shuffle(deck)
    return deck


deck = create_deck()
dealer_hand = deck.pop()
player_hand = deck.pop()


print('dealer hand >', dealer_hand)


select = int(input('your hand is high_0 low_1 : '))

high_low = dealer_hand[1] - player_hand[1]

if high_low < 0:  # player hand is high
    result = 0
# elif high_low == 0:  # draw

else:  # player hand is low
    result = 1

print(player_hand)

if select == result:
    print('you win!')
else:
    print('you lose')
