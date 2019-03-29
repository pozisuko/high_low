#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


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


def ask():
    answer = input('say, high or low:')
    return answer


def validate(answer, has_answer):
    if answer in has_answer:
        return True
    else:
        return False


def select(is_valid, answer):
    if is_valid:
        if answer == 'high':
            return True
        else:
            return False


def is_high(player_hand, dealer_hand):
    is_high = player_hand.rank - dealer_hand.rank
    if is_high > 0:
        return True
    else:
        return False


def result(high, selection):
    if is_high == 0:
        print('you lose.')
    elif high == selection:
        print('you win!')
    else:
        print('you lose.')


def main():
    deck = Deck()
    player_hand = deck.draw
    dealer_hand = deck.draw
    has_answer = ['high', 'low']

    print('dealer hand:', dealer_hand)

    answer = ask()
    is_valid = validate(answer, has_answer)

    if not is_valid:
        print('not valid input. plz input high or low.')
        return

    selection = select(is_valid, answer)
    high = is_high(player_hand, dealer_hand)

    print('your hand:', player_hand)

    result(high, selection)


if __name__ == '__main__':
    main()
