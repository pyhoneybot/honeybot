''' player class '''
# pylint: disable=E1601
class Player(object):
    ''' player class '''

    def __init__(self, nr, chips, username):
        ''' player initialization '''

        self.__position_nr = nr
        self.__general_name = 'player' + str(nr)
        self.__username = username
        self.__chips = chips
        self.__hand = []
        self.add_position(nr)

    def number(self):
        ''' show number '''

        return self.__number

    def general_name(self):
        ''' general name '''

        return self.__general_name

    def show_player_hand(self):
        ''' show hand '''

        return self.__hand

    def add_hand(self, hand):
        ''' adding hand to player '''

        self.__hand = hand

    def chips(self):
        ''' show chips '''

        return self.__chips

    def increase_chips(self, win_chips):
        ''' winning money '''

        self.__chips = self.__chips + win_chips

    def decrease_chips(self, lost_chips):
        ''' losing money '''

        self.__chips = self.__chips - lost_chips

    def position_nr(self):
        ''' show position number '''

        return self.__position_nr

    def position_name(self):
        ''' show position name '''

        return self.__position_name

    def add_position(self, position_nr):
        ''' adding position '''

        if position_nr >= 0 and position_nr <= 5:
            self.__position_nr = position_nr

            if self.__position_nr == 0:
                self.__position_name = 'Small Blind'

            elif self.__position_nr == 1:
                self.__position_name = 'Big Blind'

            elif self.__position_nr == 2:
                self.__position_name = 'Under the Gun'

            elif self.__position_nr == 3:
                self.__position_name = 'Middle'

            elif self.__position_nr == 4:
                self.__position_name = 'Tail'

            else:
                self.__position_name = 'Dealer'

        else:
            print('Position nr is too big or too little')
            pass

    def bet(self, amount):
        '''change game_init to the file where the game info is stored'''
        game_init.game[2].increase_pot(amount)
        self.decrease_chips(0)

    def get_name(self):
        '''show player's name'''

        return self.__username

    def add_card_to_hand(self,card):
        '''add a card to the player's hand'''
        index = len(self.__hand.show_hand_obj())
        self.__hand.show_hand_obj().append(card)
