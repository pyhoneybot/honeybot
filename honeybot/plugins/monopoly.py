"""
[monopoly.py]
Monopoly Plugin
[Author]
Angelo Giacco
[About]
Play monopoly
[Commands]
>>> .monopoly setup
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
"""
import monopoly_assets
import monopoly_player
import random

class Plugin:

    def __init__(self):
        pass

    def setup(self):
        pass

    def join(nickname):

    def run(self,incoming,methods,info):
        try:
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.monopoly':
        except Exception as e:
            print("woops, monopoly plugin error ",e)
