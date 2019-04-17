# -*- coding: utf-8 -*-
"""
[monopoly.py]
Monopoly Plugin
[Author]
Angelo Giacco
[About]
Play monopoly
[Commands]
>>> .monopoly create
creates monopoly

>>>.monopoly join
user joins the game

>>>.monopoly start
starts the game

>>>.monopoly roll
rolls two dice to see how far the user will move/if the user can leave the jail

>>> .monopoly buy
user purchases property

>>> .monopoly pass
user passes on the opportunity to buy a property

>>> .monopoly quit
ends the game

>>>.monopoly help
sends messages explaining how to use the monopoly plugin
"""
import monopoly_assets
import monopoly_player
import random

class Plugin:
    stage = None #none for no game yet initalised, 0 for create, 1 for already started
    game_over = False #becomes true when a player wins or when ".monopoly quit" is entered
    players = [] #stores player objects

    def __init__(self):
        pass

    def create(self):
        stage = 0

    def join(self,nickname):
        if Plugin.stage == 0:
            if nickname not in Plugin.players:
                Plugin.players.append(nickname)
                return nickname+" has been added to the monopoly game"
            else:
                return nickname+" is already in the monopoly game"
        else:
            return "a game has not yet started, use '.monopoly create'" +\
            " to create one or '.monopoly help' to find out how this plugin works"

    def run(self,incoming,methods,info):
        try:
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.monopoly':

                if not(len(msgs) == 2):
                    methods['send'](info]['address'],".monopoly requires one argument:" +\
                    " create, join, start, buy, pass or quit")

                elif msgs[0] == "create":
                    name = info["address"].split("!")[0]
                    create(self)
                    methods['send'](info['address'],"game has been created by "+name)
                    join(self,name)
                    methods['send'](info['address'],"to join this monopoly game "+\
                    "enter '.monopoly join'")

                elif msgs[1] == "join":
                    name = info["address"].split("!")[0]
                    methods['send'](info['address'],Plugin.join(self,name))

        except Exception as e:
            print("woops, monopoly plugin error ",e)
