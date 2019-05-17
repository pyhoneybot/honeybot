''' deck class '''

# pylint: disable=E1601, W0612

import random
import card

class Deck(object):
    ''' deck class '''

    colors = ['C', 'D', 'H', 'S']
    figures = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    i = 0
    for color in colors:

        for figure in figures:

            locals()['card%s' % i] = card.Card(figure + color)
            i += 1
    def __init__(self):
        ''' deck initialization '''

        self.__deck = []
        for color in self.colors:

            for figure in self.figures:

                self.__deck.append(card.Card(figure + color))

    def show_deck(self):
        ''' show deck '''

        return(" ".join([c.show_card() for c in self.__deck]))

    def nth_card(self, n):
        ''' show the n-th card from deck '''

        try:
            return self.__deck[n]
        except BaseException:
            print('Wrong index')
            return card.Card("0X")

    def draw_by_number(self, nr):
        ''' pick card from deck by nr '''

        try:
            pick = self.__deck[nr]
            if pick == "OX":
                raise BaseException
            self.__deck.remove(pick)
            return pick

        except BaseException:
            print('Wrong index')
            return card.Card("0X")

    def draw_by_name(self, name):
        ''' pick card from deck by name '''

        flag = 0
        for pick in self.__deck:

            if pick.show_card() == name:
                self.__deck.remove(pick)
                flag = 1
                break

        if flag == 0:
            print('Wrong name')
            pass

        else:
            return pick

    def make_board(self):
        ''' make a random board '''

        board = []
        for i in range(5):

            random_number = random.randint(0, len(self.__deck) - 1)
            board.append(self.draw_by_number(random_number))

        return board

    def make_hand(self):
        ''' make a random hand '''

        hand = []
        for i in range(2):

            random_number = random.randint(0, len(self.__deck) - 1)
            hand.append(self.draw_by_number(random_number))

        return hand

    def __len__(self):
        '''return the number of cards in the deck '''
        return len(self.__deck)
