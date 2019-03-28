#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import auto, Enum, IntEnum
import random
import readchar
import sys


class Deck:
    deck = []

    def __init__(self):
        suits = ['♡', '♢', '♤', '♧']
        ranks = range(2, 15)
        self.deck = [(i, j) for i in suits for j in ranks]
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()


def ask():
    answer = input('say, high or low: ')
    return answer


def validate(answer, selection):
    if answer in selection:
        return True
    else:
        return False


def is_high(player_hand, dealer_hand):
    if player_hand[1] - dealer_hand[1] > 0:
        return True
    else:
        return False


def main():
    deck = Deck()
    player_hand = deck.draw()
    dealer_hand = deck.draw()
    selection = ['high', 'low']

    print('dealer hand :', dealer_hand)

    answer = ask()
    is_valid = validate(answer, selection)

    if not is_valid:
        print('no valid input. plz input high or low.')
        return

    print('your hand :', player_hand)

    high = is_high(player_hand, dealer_hand)

    if (high and answer == 'high') or (not high and answer == 'low'):
        print('you win!')
    else:
        print('you lose.')


if __name__ == '__main__':
    main()
