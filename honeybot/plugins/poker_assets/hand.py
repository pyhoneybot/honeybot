''' hand class '''

# pylint: disable=E1601

import deuces
import best5
import board
import card

class Hand(object):
    ''' hand class '''

    def __init__(self, hand):
        ''' hand initialization '''

        self.__hand = hand
        self.__card1 = hand[0]
        self.__card2 = hand[1]

    def show_hand(self):
        ''' show hand '''

        return(" ".join([c.show_card() for c in self.__hand]))

    def show_hand_obj(self):
        ''' show hand object '''

        return self.__hand

    def best_five(self, b):
        ''' best 5 out of 7 '''

        hand_and_board = self.show_hand() + ' ' + b.flop1() + ' ' + b.flop2() + \
        ' ' + b.flop3() + ' ' + b.turn() + ' ' + b.river()

        return( " ".join([c for c in best5.test_best_hand(hand_and_board)]))

    def hand_strength(self, board):
        ''' hand strength '''

        evaluator = deuces.Evaluator()
        b5 = self.best_five(board)
        h1 = b5[:2].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        h2 = b5[3:5].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        b1 = b5[6:8].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        b2 = b5[9:11].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        b3 = b5[12:14].replace('S', 's').replace('H', 'h').replace('D', 'd').replace('C', 'c')
        hl = [deuces.Card.new(h1), deuces.Card.new(h2)]
        bl = [deuces.Card.new(b1), deuces.Card.new(b2), deuces.Card.new(b3)]
        strength = evaluator.evaluate(bl, hl)

        return strength
