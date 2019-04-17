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
    Plugin.stage = None #none for no game yet initalised, 0 for create, 1 for already started
    Plugin.game_over = False #becomes true when a player wins or when ".monopoly quit" is entered
    Plugin.players = [] #stores player objects
    Plugin.next = "start" #if this has a command the next .monopoly command must either be help, quit or this one.

    def __init__(self):
        pass

    def count_player_properties(player):
        #creates a dictionary with the users properties from the portfolio list
        #utilises the fact that True is equal to 1
        violet = sum(property.color == "Violet" for property in player.getPortfolio())
        light_blue = sum(property.color == "Light blue" for property in player.getPortfolio())
        purple = sum(property.color == "Purple" for property in player.getPortfolio())
        orange = sum(property.color == "Orange" for property in player.getPortfolio())
        red = sum(property.color == "Red" for property in player.getPortfolio())
        yellow = sum(property.color == "Yellow" for property in player.getPortfolio())
        green = sum(property.color == "Green" for property in player.getPortfolio())
        blue = sum(property.color == "Blue" for property in player.getPortfolio())
        prop_count_dict = {"Violet":violet,
                           "Light blue":light_blue,
                           "Purple":purple,
                           "Orange":orange,
                           "Red":red,
                           "Yellow":yellow,
                           "Green":green,
                           "Blue":blue}
        return prop_count_dict

    def get_info(self,methods,info):
        for player in Plugin.players:
            portfolio = player.getPortfolio()
            name = player.getName()
            pot = player.getPot()
            if len(portfolio) > 0:
                portfolio_dict = count_player_properties
                for key in portfolio_dict.keys():
                    if portfolio_dict[key] != 0:
                        message = name+' has '+str(portfolio_dict[key]) + " " + key + " properties"
                        methods['send'](info['address'],message)
                    else:
                        continue
            else:
                message = name+" has no properties"
                methods['send'](info['address'],message)
            methods['send'](info['address'],name+"'s pot is "+str(pot))

    def create(self):
        Plugin.stage = 0
        print("stage = "+str(Plugin.stage))

    def join(self,nickname):
        if Plugin.stage == 0:
            if nickname not in Plugin.players:
                Plugin.players.append(Player(nickname))
                return nickname+" has been added to the monopoly game"
            else:
                return nickname+" is already in the monopoly game"
        else:
            return "a game has not yet started, use '.monopoly create'" +\
            " to create one or '.monopoly help' to find out how this plugin works"

    def start(self,methods,info):
        random.shuffle(Plugin.players)
        methods["send"](info["address"],"The monopoly game has started, player order has been randomly generated:")
        for player in Plugin.players:
            name = player.getName()
            methods["send"](info["address"],name)
        get_info(methods,info)
        turn = 0
        turn_player = Plugin.players[turn].getName()
        methods["send"](info["address"],"first up is "+turn_player)
        Plugin.next = "roll"

    def quit(self):
        if Plugin.stage == None:#may be self.stage
            return "no game has started yet"
        else:
            Plugin.stage == None
            Plugin.players = []
            Plugin.next = "start"
            return "game quit"


    def run(self,incoming,methods,info):
        try:
            msgs = info['args'][1:][0].split(" ")
            print("msgs")
            print(msgs)
            if info['command'] == 'PRIVMSG' and msgs[0] == '.monopoly':

                if not(len(msgs) == 2):
                    methods['send'](info['address'],".monopoly requires one argument:" +\
                    " create, join, start, buy, pass or quit")

                elif msgs[1].lower() == "create":
                    print("create if statement")
                    name = info["address"].split("!")[0]
                    create(self)
                    methods['send'](info['address'],"game has been created by "+name)
                    methods['send'](info['address'],Plugin.join(self,name)) #automatically adds the creator
                    methods['send'](info['address'],"to join this monopoly game "+\
                    "enter '.monopoly join'")

                elif msgs[1].lower() == "join":
                    name = info["address"].split("!")[0]
                    methods['send'](info['address'],Plugin.join(self,name))

                elif msgs[1].lower() == "start":
                    Plugin.start(self,methods,info)
                    
                elif msgs[1].lower() == "roll":

                elif msgs[1].lower() == "buy":

                elif msgs[1].lower() == "pass":

                elif msgs[1].lower() == "quit":
                    methods['send'](info['address'],Plugin.quit(self))

        except Exception as e:
            print("woops, monopoly plugin error ",e)
