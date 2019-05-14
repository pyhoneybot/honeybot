''' board class '''

# pylint: disable=E1601

class Board(object):
    ''' board class '''

    def __init__(self, board):
        ''' board initialization '''

        self.__board = board
        self.__flop = board[:3]
        self.__flop1 = board[0]
        self.__flop2 = board[1]
        self.__flop3 = board[2]
        self.__turn = board[3]
        self.__river = board[4]

    def show_board(self):
        ''' show board '''
        return(" ".join([c.show_card() for c in self.__board]))

    def flop(self):
        ''' show flop '''

        return(" ".join([c.show_card() for c in self.__flop]))

    def flop1(self):
        ''' show flop1 '''

        return self.__flop1.show_card()

    def flop2(self):
        ''' show flop2 '''

        return self.__flop2.show_card()

    def flop3(self):
        ''' show flop3 '''

        return self.__flop3.show_card()

    def turn(self):
        ''' show turn '''

        return self.__turn.show_card()

    def river(self):
        ''' show river '''

        return self.__river.show_card()

    def __len__(self):
        return len(self.__board)
