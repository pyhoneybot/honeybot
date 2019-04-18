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
user purchases property if unowned, otherwise buys house

>>> .monopoly pass
user passes on the opportunity to buy a property if unowned, or on the opportunity to buy a house

>>> .monopoly quit
ends the game

>>>.monopoly help
sends messages explaining how to use the monopoly plugin

>>>.monopoly gameinfo
sends messages showing the status of each player
"""
import monopoly_assets
import monopoly_player
import random

class Plugin:
    Plugin.stage = None #none for no game yet initalised, 0 for create, 1 for already started
    Plugin.game_over = False #becomes true when a player wins or when ".monopoly quit" is entered
    Plugin.players = [] #stores player objects
    Plugin.create_req = True #create command required
    Plugin.decision_req = False #buy or pass command required
    Plugin.start_join_req = False #start game or join game required
    Plugin.roll_req = False

    def __init__(self):
        pass

    def count_color_property(portfolio, col):
        properties = [asset for asset in portfolio if isinstance(asset,Property)]
        return sum(property.color == col for property in properties)

    def count_utilities(portfolio):
        return len([utility for utility in portfolio if isinstance(utility,Utility)])

    def count_railroads(portfolio):
        return len([railroad for railroad in portfolio if isinstance(railroad,Railroad)])

    def count_player_properties(player):
        #creates a dictionary with the users properties from the portfolio list
        #utilises the fact that True is equal to 1
        portfolio = player.getPortfolio()

        violet = count_color_property(portfolio, "Violet")
        light_blue = count_color_property(portfolio, "Light blue")
        purple = count_color_property(portfolio, "Purple")
        orange = count_color_property(portfolio, "Orange")
        red = count_color_property(portfolio, "Red")
        yellow = count_color_property(portfolio, "Yellow")
        green = count_color_property(portfolio, "Green")
        blue = count_color_property(portfolio, "Blue")
        utilities = count_utilities(portfolio)
        railroads = count_railroads(portfolio)
        prop_count_dict = {"Violet":violet,
                           "Light blue":light_blue,
                           "Purple":purple,
                           "Orange":orange,
                           "Red":red,
                           "Yellow":yellow,
                           "Green":green,
                           "Blue":blue,
                           "Utility":utilities,
                           "Railroad":railroads}
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
            ##should also show player location

    def find_owner(asset_name):
        for player in Plugin.players:
            for property in player.getPortfolio():
                if property.name == asset_name:
                    return [True,Plugin.players.index(player)]
                else:
                    return [False]

    def create(self,methods,info):
        if Plugin.create_req:
            Plugin.stage = 0
            Plugin.create_req = False
            Plugin.start_join_req = True
            print("stage = "+str(Plugin.stage))
        else:
            methods["send"](info["address"],"Game ")

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
        if Plugin.start_join_req:
            random.shuffle(Plugin.players)
            methods["send"](info["address"],"The monopoly game has started, player order has been randomly generated:")
            for player in Plugin.players:
                name = player.getName()
                methods["send"](info["address"],name)
            get_info(methods,info)
            turn = 0
            turn_player = Plugin.players[turn].getName()
            methods["send"](info["address"],"first up is "+turn_player)
            Plugin.roll_req = True
            Plugin.start_join_req = False
        else:
            methods["send"](info["address"],"This command is currently not possible")

    def get_rent(self, asset, asset_owner, moveamount):
        if isinstance(asset,Property):
            #num_prop_in_set = len([property for property in asset_owner.getPortfolio() if property.color == asset.color])
            return asset.rents[asset.house_count]

        elif isinstance(self,asset, Utility):
            num_util = len([property for property in asset_owner.getPortfolio() if isinstance(property,Utility])
            calc_string = asset.rents[num_util] + " " + str(move_amount)
            return eval(calc_string)

        elif isinstance(self,asset, Railroad):

    def roll(self):
        move_amount = random.randint(1,6) + random.randint(1,6)
        player = Plugin.players[turn]
        passed_go = player.update_position(move_amount)
        new_location = board_spaces[player.getPosition()]
        methods["send"](info['address'],player.name+" rolled "+str(move_amount) +\
        " and is now located at "+new_location.name)
        new_location_owned = find_owner(new_location.name)
        if new_location_owned[0]:
            owner = Plugin.players[new_location_owned[1]]
            if player.name == owner:
                ##buy a house option
                cost_house = get_cost_house(self,asset):
            else:
                #must figure out fee
                #find a way to find out the number of houses owned
                #possibly create a self.house_count in Property class
                #this is your work for tomorrow
                #also consider .monopoly info command rather than always printing
                methods["send"](info['address'],player.name+" landed on a property owned by "+\
                owner.name)
                rent = get_rent(self,new_location,owner,move_amount)
        else:
            #buy option



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
                    " create, join, start, buy, pass, gameInfo, help or quit")

                elif msgs[1].lower() == "create":
                    print("create if statement")
                    name = info["address"].split("!")[0]
                    create(self,methods,info)
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
                    Plugin.roll(self,methods,info)

                elif msgs[1].lower() == "help":
                    Plugin.help(self,methods,info)

                elif msgs[1].lower() == "gameinfo":
                    Plugin.get_info(self,methods,info)

                elif msgs[1].lower() == "buy":
                    pass

                elif msgs[1].lower() == "pass":
                    pass

                elif msgs[1].lower() == "quit":
                    methods['send'](info['address'],Plugin.quit(self))

                else:
                    methods['send'](info['address'],".monopoly requires one argument:" +\
                    " create, join, start, buy, pass, gameInfo, help or quit")

        except Exception as e:
            print("woops, monopoly plugin error ",e)
