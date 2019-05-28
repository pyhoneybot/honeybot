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

>>>.blackjack start
start a round

>>>.blackjack hit
get another card

>>>.blackjack stand
move on to next player
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
    turn = 0
    player_lst = []
    starting_chips = 100
    winner = None
    end = False


    def __init__(self):
        pass

    """
    USEFUL FUNCTIONS
    """

    def next_turn(methods,info):
        ''' increment turn and find winner if hitting and standing over '''

        try:
            Plugin.turn += 1
            if Plugin.turn == len(Plugin.player_lst):
                #all players have find winner
                total_lst = [player.show_player_hand().hand_total() for player in Plugin.player_lst]
                index,value = max(list(enumerate(total_lst)), key=lambda x:x[1])
                if total_lst.count(value) == 1:
                    Plugin.winner = Plugin.player_lst[index].get_name()
                    methods["send"](info["address"],"The winner is "+Plugin.winner+"!")
                else:
                    methods["send"](info["address"],"This round has ended in a draw!")
                Plugin.bj_created = False
        except Exception as e:
            print("woops, blackjack turn change error ",e)

    def initPlayer(methods,info):
        ''' add a player to the round '''

        if Plugin.bj_created:
            if not Plugin.round_started:
                name = info["prefix"].split("!")[0]
                if len(Plugin.player_lst) <= 5: #limit game to 6 players
                    if not(name in [player.get_name() for player in Plugin.player_lst]):
                        Plugin.player_lst.append(player.Player(len(Plugin.player_lst),Plugin.starting_chips,name))
                        methods["send"](info["address"],name+" joined the game!")
                    else:
                        methods["send"](info["address"],"You are already in this round!")
                else:
                    methods["send"](info["address"],"This round is full already")
            else:
                methods["send"](info["address"],"The round has started, wait for a new one to join!")
        else:
            methods["send"](info["address"],"A game has not yet been created!")

    def checkHand(methods,info,player):
        ''' check the value of a player's hand '''

        name = player.get_name()
        total = player.show_player_hand().hand_total()
        cards = " ".join([card.show_card() for card in player.show_player_hand().show_hand_obj()])
        if total > 21:
            methods["send"](info["address"],name+"'s hand "+cards+" has a value of "+str(total)+" so you have been kicked out")
            for p in Plugin.player_lst:
                if p.get_name() == name:
                    Plugin.player_lst.remove(p)
            if len(Plugin.player_lst) == 1:
                Plugin.winner = Plugin.player_lst[0].get_name()
                methods["send"](info["address"],"The winner is "+Plugin.winner+"!")
                Plugin.bj_created = False
        elif total == 21:
            methods["send"](info["address"],name+"'s hand "+cards+" has a value of 21 so you have won!")
            Plugin.winner = name
            Plugin.bj_created = False
        else:
            methods["send"](info["address"],name+"'s hand "+cards+" has a value of "+str(total)+".")

    """
    COMMAND FUNCTIONS
    """

    def initGame(methods,info):
        ''' create a new round '''

        if not Plugin.bj_created:
            Plugin.turn = 0
            Plugin.winner = None
            Plugin.player_lst = []
            name = info["prefix"].split("!")[0]
            Plugin.bj_created = True
            Plugin.round_started = False
            Plugin.initPlayer(methods,info)
            Plugin.DECK = deck.Deck()
            methods["send"](info["address"],name+" has started a game of blackjack! Use .blackjack join to join in!")
        else:
            methods["send"](info["address"],"A game already exists!")

    def start(methods,info):
        ''' start the game '''

        Plugin.round_started = True
        Plugin.bj_created = True
        for player in Plugin.player_lst:
            player.add_hand(hand.Hand(Plugin.DECK.make_hand()))
            total = player.show_player_hand().hand_total()
            cards = " ".join([card.show_card() for card in player.show_player_hand().show_hand_obj()])
            Plugin.checkHand(methods,info,player)

    def hit(methods,info):
        ''' give player a new card '''

        name = info["prefix"].split("!")[0]
        if Plugin.winner == None:
            if Plugin.player_lst[Plugin.turn].get_name() == name:
                Plugin.player_lst[Plugin.turn].add_card_to_hand(Plugin.DECK.draw_random_card())
                Plugin.checkHand(methods,info,Plugin.player_lst[Plugin.turn])
            else:
                methods["send"](info["address"],"It is not your turn!")
        else:
            methods["send"](info["address"],"The round is already over and has been won by "+Plugin.winner)

    def stand(methods,info):
        ''' player chooses not to get a new car '''
        name = info["prefix"].split("!")[0]
        if Plugin.winner == None:
            if Plugin.turn < len(Plugin.player_lst):
                if Plugin.player_lst[Plugin.turn].get_name() == name:
                    methods["send"](info["address"],info["prefix"].split("!")[0]+" has chosen not to pick another card!")
                    Plugin.next_turn(methods,info)
                else:
                    methods["send"](info["address"],"It is not your turn!")
            else:
                methods["send"](info["adress"],"something went wrong, please try restarting")
                Plugin.bj_created = False
        else:
            methods["send"](info["address"],Plugin.winner+" has already won the game!")

    """
    RUNNING PLUGIN
    """

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1:][0].split()
            if info['command'] == 'PRIVMSG' and (msgs[0] == ".bj" or msgs[0] == ".21" or msgs[0] == ".blackjack") and len(msgs) == 2:
                if msgs[1] == "create":
                    Plugin.initGame(methods,info)
                elif msgs[1] == "join":
                    Plugin.initPlayer(methods,info)
                elif msgs[1] == "start":
                    Plugin.start(methods,info)
                elif msgs[1] == "hit":
                    Plugin.hit(methods,info)
                elif msgs[1] == "stand":
                    Plugin.stand(methods,info)
                else:
                    methods["send"](info["address"],"invalid blackjack command")
        except Exception as e:
            print('woops blackjack plugin error: ', e)
