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

>>> .monopoly leave
user leaves the game

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
    Plugin.game_over = False #becomes true when a player wins
    #also becomes true when one player left bot not implemented yet because not practical for testing
    Plugin.players = [] #stores player objects
    Plugin.create_req = True #create command required
    Plugin.decision_req = False #buy or pass command required
    Plugin.start_join_req = False #start game or join game required
    Plugin.roll_req = False #roll required
    Plugin.buy_pass_req = False #buy or pass required


    def __init__(self):
        pass


    """
    USEFUL FUNCTIONS
    """

    def next_turn(self):
        pass


    def count_color_property(portfolio, col):
        properties = [asset for asset in portfolio if isinstance(asset,Property)]#util and railroad do not have color
        return sum(property.color == col for property in properties) #True is equal to 1 in python


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
            portfolio = player.getPortfolio()#returns array
            name = player.getName()
            pot = player.getPot()#returns string

            if len(portfolio) > 0:
                portfolio_dict = count_player_properties(player)
                for key in portfolio_dict.keys():

                    if portfolio_dict[key] != 0:
                        message = name+' has '+str(portfolio_dict[key]) + " " + key + " properties"
                        methods['send'](info['address'],message)
                    else:
                        continue

            else:
                message = name+" has no properties"
                methods['send'](info['address'],message)
            methods['send'](info['address'],name+"'s pot is "+pot)

            if player.getPosition() == 10 && player.imprisoned:
                methods['send'](info['address'],name+" is locked in jail")
            elif player.getPosition() == 10 && not player.imprisoned:
                methods['send'](info['address'],name+" is at the joil but not inside... yet")
            if player.imprisoned:
                location = board_spaces[player.getPosition()].get_name()
                methods['send'](info['address'],name+" is at "+location)


    def get_help(self,methods,info):
        methods['send'](info['address'],"'.monopoly create' creates a new game people can join.")
        methods['send'](info['address'],"'.monopoly start' starts the game. People can no longer join.")
        methods['send'](info['address'],"'.monopoly roll' rolls two dice and move on the board.")
        methods['send'](info['address'],"'.monopoly buy' buys the property where you are on the board or buy a house for the property.")
        methods['send'](info['address'],"'.monopoly pass' refuses to buy the property or house for the property.")
        methods['send'](info['address'],"'.monopoly leave' leaves the game")
        methods['send'](info['address'],"'.monopoly gameinfo' gets information about each player.")
        methods['send'](info['address'],"Hope this helps!")


    def find_owner(asset_name):
        for player in Plugin.players:
            for property in player.getPortfolio():
                if property.get_name() == asset_name:
                    return [True,Plugin.players.index(player)]
                else:
                    return [False]

    def get_rent(self, asset, asset_owner, move_amount):
        if isinstance(asset,Property):
            #find a way to find out the number of properties owned in a set
            #num_prop_in_set = len([property for property in asset_owner.getPortfolio() if property.color == asset.color])
            return asset.rents[asset.house_count]

        elif isinstance(self,asset, Utility):
            num_util = len([property for property in asset_owner.getPortfolio() if isinstance(property,Utility)])
            calc_string = asset.rents[num_util] + " " + str(move_amount)
            return eval(calc_string)

        elif isinstance(self,asset, Railroad):
            num_rail = len([property for property in asset_owner.getPortfolio() if isinstance(property,Railroad)])
            return asset.rents[num_rail]

    """
    COMMUNITY CARD AND CHANCE METHODS
    """

    def earn(methods,info,player,amount):
        player.increasePot(amount)
        methods["send"](info["address"],player.getName()+" now has a pot of "+player.getPot())

    def get_outta_jail(methods,info,player):
        if player.imprisoned:
            player.imprisoned = False
            player.prison_time = 0
            methods["send"](info["address"],player.getName()+" escaped the jail")
        else:
            player.get_outta_jail_card = True

    def collect(methods,info,player,amount):
        for opponent in Plugin.players:#will iterate over player as well
            if player != opponent:
                opponent_alive = opponent.reducePot(amount)
                player.increasePot(amount)
                if opponent_alive:
                    methods["send"](info["address"],player.getName()+" received "+\
                    str(amount)+" from "+opponent.getName())
                else:
                    methods["send"](info["address"],player.getName()+" took all of "+\
                    opponent.getName()+"'s money and so "+opponent.getName()+" has left the game")

    def go(methods,info,player):
        player.setPosition(0)
        player.increasePot(200)

    def jail(methods,info,player):
        if player.get_outta_jail_card:
            methods["send"](info["address"],player.getName()+" used his get out of jail free card!")
            player.setPosition(10)
        else:
            player.setPosition(10)
            player.imprisoned = True

    def repairs(methods,info,player,house_fee,hotel_fee):
        property_list = [asset for asset in player.getPortfolio() if isinstance(asset,Property)]
        hotel_total = 0
        house_total = 0
        for property in property_list:
            if property.house_count == 5:
                hotel_total += 1
            else:
                house_total += property.house_count

        cost = house_fee * house_total + hotel_fee * hotel_total
        player_alive = player.reducePot(cost)

        if player_alive:
            methods["send"](info["address"],player.getName+" was forced to spend "+\
            +str(cost)+" on repairs and now has "+player.getPot())
        else:
            methods["send"](info["address"],player.getName+" was forced to spend "+\
            +str(cost)+" on repairs and now has no more money and so has left the game")
            Plugin.players.remove(player)

    def fine(methods,info,player,amount):
        #must do this tomorrow


    """
    PLUGIN COMMANDS
    """

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


    def roll(self,methods,info):
        move_amount = random.randint(1,6) + random.randint(1,6)
        player = Plugin.players[turn]
        passed_go = player.update_position(move_amount)
        new_location = board_spaces[player.getPosition()]
        methods["send"](info['address'],player.getName()+" rolled "+str(move_amount) +\
        " and is now located at "+new_location.get_name())
        new_location_owned = find_owner(new_location.get_name())
        if new_location_owned[0]:##if property is owned by somebody
            owner = Plugin.players[new_location_owned[1]]

            if player.getName() == owner:
                ##buy a house option

                if isinstance(new_location,Property):
                    num_prop_in_set = count_player_properties(player)[new_location.color]

                    if num_prop_in_set == Property.set_houses[new_location.color]:
                        cost_house = new_location.get_house_cost()
                        methods["send"](info["address"],"You have landed on your own property."+\
                        "and can buy a house for "+str(cost_house))
                        #should show property information and user pot
                        Plugin.buy_pass_req = True
                        Plugin.roll_req = False
                        #maybe add house info or summat to know what is being bought

                    else:
                        methods["send"](info["address"],"You have landed on your own property."+\
                        "but cannot buy a house as you need a full set")
                        next_turn()

                else:
                    methods["send"](info["address"],"You have landed on your own property "+\
                    "but you cannot buy houses for railroads or utilities")
                    next_turn()

            else:
                rent = get_rent(self,new_location,owner,move_amount)
                methods["send"](info['address'],player.getName()+" landed on a property owned by "+\
                owner.getName()+" and must pay them "+str(rent))
                player_alive = player.reducePot(rent)
                owner.increasePot(rent)

                if player_alive:
                    methods["send"](info['address'],player.getName+" now only has "+player.getPot() +\
                    "whereas "+owner.getName()+" now has "+owner.getPot()
                    next_turn()

                else:
                    methods["send"](info['address'],player.getName+" is now out of the game "+\
                    "whereas "+owner.getName()+" now has "+owner.getPot()
                    Plugin.players.remove(player)
                    next_turn()

        elif isinstance(new_location,Property) or isinstance(new_location,Utility) or isinstance(new_location,Railroad):
            #buy
            Plugin.buy_pass_req = True
            Plugin.roll_req = False
            methods["send"](info['address'],"You have landed on an unowned asset"+\
            "which you may buy for "+str(new_location.price))
            #methods["send"](info["address"],getInfo(new_location))
            #something like the line above should be executed to give the user an idea
            #about what they are buying and the rest of their situation
            #such as ownership of other properties in that set and how much money they have

        elif player.getPosition() == 2 or player.getPosition() == 17 or player.getPosition() == 33:
            #take community Card
            community_card_methods = [
                                      earn,
                                      get_outta_jail,
                                      collect,
                                      go,
                                      jail,
                                      repairs,
                                      fine
                                     ]
            #must pick first in array, place it at back, and execute its function with correct args.
            next_turn()

        elif player.getPosition() == 7 or player.getPosition() == 22 or player.getPosition() == 36:
            #take chance card
            next_turn()

        elif player.getPosition() == 30:
            #check player has a get out of jail card
            if player.get_outta_jail_card:
                player.get_outta_jail_card = False
                methods["send"](info["address"],name+" landed on go to jail but used his get out of jail card...")
                next_turn()

            else:
                player.setPosition(10)
                player.imprisoned = True
                next_turn()

        elif player.getPosition == 38:
            player_alive = player.reducePot(100)
            if player_alive:
                methods["send"](info["address"],name+" landed on luxury tax and had to pay"+\
                " 100 in tax and so now has "+player.getPot())

            else:
                methods["send"](info["address"],name+" landed on luxury tax and had to pay"+\
                " 100 in tax but did not have enough many so is no longer in the game...")
                Plugin.players.remove(player)

            next_turn()

        elif player.getPosition == 4:
            player_alive = player.reducePot(200)
            if player_alive:
                methods["send"](info["address"],name+" landed on luxury tax and had to pay"+\
                " 200 in tax and so now has "+player.getPot())

            else:
                methods["send"](info["address"],name+" landed on luxury tax and had to pay"+\
                " 200 in tax but did not have enough many so is no longer in the game...")
                players.remove(player)

            next_turn()

        else:
            next_turn()


    def leave(self,player):
        #change to quit a single user
        if Plugin.stage == None:#may be self.stage
            return "no game has started yet"
        if player not in players:
            return "you are not playing in this game!"
        else:
            players.remove(player)
            return player.getName() +" has left the game"

    """
    RUN PLUGIN
    """

    def run(self,incoming,methods,info):
        try:
            msgs = info['args'][1:][0].split(" ")
            print("msgs")
            print(msgs)
            if info['command'] == 'PRIVMSG' and msgs[0] == '.monopoly':

                if not(len(msgs) == 2):
                    methods['send'](info['address'],".monopoly requires one argument:" +\
                    " create, join, start, buy, pass, gameInfo, help or leave")

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
                    Plugin.get_help(self,methods,info)

                elif msgs[1].lower() == "gameinfo":
                    Plugin.get_info(self,methods,info)

                elif msgs[1].lower() == "buy":
                    pass

                elif msgs[1].lower() == "pass":
                    next_turn()

                elif msgs[1].lower() == "leave":
                    methods['send'](info['address'],Plugin.leave(self,Plugin.players[turn]))

                else:
                    methods['send'](info['address'],".monopoly requires one argument:" +\
                    " create, join, start, buy, pass, gameInfo, help or leave")

        except Exception as e:
            print("woops, monopoly plugin error ",e)
