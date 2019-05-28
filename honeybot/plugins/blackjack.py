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

>>>.blackjack leave
leave the game
"""
import random,sys,os
sys.path.append('plugins/poker_assets')
import deck
import card
import hand
import player

class Plugin():

    bj_created = False
    round_started = False
    dec_req = False
    turn = 0
    player_lst = []
    starting_chips = 100
    winner = None


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

    def initPlayer(methods,info):
        '''add a player to the round'''

        name = info["prefix"].split("!")[0]
        if len(Plugin.player_lst) <= 5: #limit game to 6 players
            if not(name in Plugin.player_lst):
                Plugin.player_lst.append(player.Player(len(Plugin.player_lst),Plugin.starting_chips,name))
                methods["send"](info["address"],name+" joined the game!")
            else:
                methods["send"](info["address"],"You are already in this round!")
        else:
            methods["send"](info["address"],"This round is full already")

    def checkHand(methods,info,player):
        '''check the value of a player's hand'''



    """
    COMMAND FUNCTIONS
    """

    def initGame(methods,info):
        '''create a new round'''

        if not Plugin.bj_created:
            Plugin.player_lst = []
            name = info["prefix"].split("!")[0]
            Plugin.initPlayer(methods,info)
            Plugin.bj_created = True
            Plugin.round_started = False
            Plugin.DECK = deck.Deck()
            methods["send"](info["address"],name+" has started a game of blackjack! Use .blackjack join to join in!")
        else:
            methods["send"](info["address"],"A game already exists!")

    def start(methods,info):
        '''start the game'''

        Plugin.round_started = True
        Plugin.bj_created = True
        Plugin.dec_req = True
        for player in Plugin.player_lst:
            player.add_hand(hand.Hand(Plugin.DECK.make_hand()))
            methods["send"](info["address"],"Showing hand of "+player.get_name())
            total = player.show_player_hand().hand_total()
            cards = " ".join([card.show_card() for card in player.show_player_hand().show_hand_obj()])
            methods["send"](info["address"],"Here is the hand: "+cards+" which have a total value of "+str(total))
            if total == 21:
                methods["send"](info["address"],player.get_name()+" has a hand worth 21 and so has won!")
                Plugin.winner = player.get_name()
            #should send each user their hand

    def hit(methods,info):
        name = info["prefix"].split("!")[0]
        if Plugin.player_lst[turn].get_name() == name:
            if Plugin.winner == None:
                player_lst[turn].add_card_to_hand(deck.draw_random_card())
                Plugin.checkHand(methods,info,player_lst[turn])
            else:
                methods["send"](info["address"],"The round is already over and has been won by "+Plugin.winner)
        else:
            methods["send"](info["address"],"It is not your turn!")


    """
    RUNNING PLUGIN
    """

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()
            if info['command'] == 'PRIVMSG' and (msgs[0] == ".bj" or msgs[0] == ".21" or msgs[0] == ".blackjack"):
                if msgs[1] == "create":
                    Plugin.initGame(methods,info)
                elif msgs[1] == "join":
                    Plugin.initPlayer(methods,info)
                elif msgs[1] == "start":
                    Plugin.start(methods,info)
                elif msgs[1] == "hit":
                    Plugin.hit(methods,info)
                elif msgs[1] == "stand":
                    methods["send"](info["address"],info["prefix"].split("!")[0]+" has chosen not to pick another card!")
                    Plugin.next_player(methods,info)
                elif msgs[1] == "leave":
                    Plugin.remove(methods,info)
                else:
                    methods["send"](info["address"],"invalid")
        except Exception as e:
            print('woops blackjack plugin error: ', e)
