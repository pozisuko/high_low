#!/usr/bin/env python3

import random


def create_deck():
    suits = ['♡', '♢', '♤', '♧']
    ranks = range(1, 14)
    deck = [(i, j) for i in suits for j in ranks]
    random.shuffle(deck)
    return deck


def validate(select):
    if 0 > select or select > 2:
        return False
    else:
        return True


def print_result():

    print(player_hand)

    if select == result:
        print('you win!')
    else:
        print('you lose')


deck = create_deck()
dealer_hand = deck.pop()
player_hand = deck.pop()


print('dealer hand: ', dealer_hand)
select = int(input('your hand is high_0 low_1: '))

if validate(select) == True:
    result = dealer_hand[1] - player_hand[1]

    if result < 0:  # win
        result = 0
        print_result()

    elif result == 0:  # draw
        print(player_hand)
        print('draw')

    else:  # lose
        result = 1
        print_result()

else:
    print('select 0 or 1 only')
