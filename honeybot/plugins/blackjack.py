# -*- coding: utf-8 -*-
"""
[blackjack.py]
Blackjack Plugin
[Author]
Angelo Giacco
[About]
Play blackjack
[Commands]
>>>.blackjack create
creates blackjack game

>>>.blackjack join
join blackjack game

>>>.blackjack round
start a round

>>>.blackjack hit
get another card

>>>.blackjack stand
move on to next player

>>>.blackjack leave the game
"""

from poker_assets import card
from poker_assets import deck
from poker_assets import hand
from poker_assets import player

class Plugin():

    bj_created = False
    round_started = False
    dec_req = False
    turn = 0
    player_lst = []


    def __init__(self):
        pass

    """
    USEFUL FUNCTIONS
    """

    def next_turn():
        '''increment turn and set to start if will cause index error'''
        try:
            Plugin.turn += 1
            if Plugin.turn == len(Plugin.player_lst):
                Plugin.turn -= len(Plugin.player_lst)
        except Exception as e:
            print("woops, poker turn change error ",e)

    def initPlayer(self,methods,info):
        '''add a player to the round'''

        name = info["prefix"].split("!")[0]
        if len(Plugin.player_lst) <= 5: #limit game to 6 players
            Plugin.player_lst.append(player.Player(len(Plugin.player_lst),Plugin.starting_chips,name))
        else:
            methods["send"](info["address"],"This round is full already")

    """
    COMMAND FUNCTIONS
    """

    def initGame(self,methods,info):
        '''create a new round'''

        print("hit game")
        if not Plugin.bj_created:
            Plugin.player_lst = []
            name = info["prefix"].split("!")[0]
            Plugin.initPlayer()
            Plugin.bj_created = True
            Plugin.round_started = False
            DECK = deck.Deck()
            methods["send"](info["address"],name+" has started a game of blackjack! Use .blackjack join to join in!")
        else:
            methods["send"](info["address"],"A game already exists!")

    def start(self,methods,info):
        '''start the game'''
        Plugin.round_started = True
        Plugin.bj_created = True
        Plugin.dec_req = True
        for player in Plugin.player_lst:
            player.add_hand(hand.Hand(DECK.make_hand()))
            methods["send"](info["address"],"Showing hand of "+player.username())
            total = player.show_hand_obj().hand_total()
            cards = ""
            for card in player.show_hand_obj():
                cards += card.show_card()
            methods[send](info["address"],"Here is the hand:"+cards+" which have a total value of "+int(total))
            #should send each user their hand
        methods["send"](info["address"],"Here is the board of the game: "+BOARD.show_board())

    """
    RUNNING PLUGIN
    """

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()
            print(msgs)
            if info['command'] == 'PRIVMSG' and (msgs[0] == ".bj" or msgs[0] == ".21" or msgs[0] == ".blackjack"):
                print("hit")
                if msgs[1] == "create":
                    Plugin.initGame(methods,info)
                elif msgs[1] == "join":
                    Plugin.initPlayer(methods,info)
                elif msgs[1] == "start":
                    Plugin.start(methods,info)
                else:
                    methods["send"](info["address"],"invalid")
        except Exception as e:
            print('woops blackjack plugin error: ', e)
