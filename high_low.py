#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys


class Card:
    SUITS = '♡♢♤♧'
    RANKS = '0 2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'{Card.SUITS[self.suit]} {Card.RANKS[self.rank]}'


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4)
                      for rank in range(1, 14)]
        random.shuffle(self.cards)

    @property
    def draw(self):
        return self.cards.pop()


class MyError(Exception):
    pass


class InputError(MyError):
    pass

 # ??????????????


def ask():

    def validate(answer):
        x = [0, 1]
        if not answer in x:
            raise InputError(answer)
        return answer

    try:
        answer = int(input('press the 1 or 0 key. high(1) / low(0): '))
        validate(answer)
        return answer

    except (InputError, ValueError, TypeError):
        print('invalid input. please enter 0 or 1 as a number.')
        exit()


def is_high(player_hand, dealer_hand):
    is_high = player_hand.rank - dealer_hand.rank
    if is_high > 0:
        return True
    else:
        return False


def result(answer, high):
    if is_high == 0:
        print('you lose.')
    elif answer ^ high:
        print('you lose.')
    else:
        print('you win!')


def main():
    deck = Deck()
    player_hand = deck.draw
    dealer_hand = deck.draw

    print('dealer hand:', dealer_hand)
    # ask()
    answer = ask()
    high = is_high(player_hand, dealer_hand)

    print('your hand:', player_hand)

    result(answer, high)


if __name__ == '__main__':
    main()
