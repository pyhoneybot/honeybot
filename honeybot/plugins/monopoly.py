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
        try:
            turn += 1
            if turn >= len(players):
                turn -= len(players)
        except Exception as e:
            print("woops, monopoly turn change error ",e)


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


    def find_owner(self,asset_name):
        for player in Plugin.players:
            for property in player.getPortfolio():
                if property.get_name() == asset_name:
                    return [True,player]
                else:
                    return [False]

    def get_rent(self, asset, asset_owner, move_amount):
        if isinstance(asset,Property):
            return asset.rents[asset.house_count]

        elif isinstance(self,asset, Utility):
            num_util = len([property for property in asset_owner.getPortfolio() if isinstance(property,Utility)])
            calc_string = asset.rents[num_util] + " " + str(move_amount)
            return eval(calc_string)

        elif isinstance(self,asset, Railroad):
            num_rail = len([property for property in asset_owner.getPortfolio() if isinstance(property,Railroad)])
            return asset.rents[num_rail]

    def move_to_space(self,methods, info, player,space):
        if player.getPosition() > board_spaces.index(space) and player.getPosition < 39:
            methods["send"](info["address"],player.getName()+" passed go moving to "+space.get_name())
            player.increasePot(200)
            player.setPosition(board_spaces.index(space))
        elif player.getPosition == board_spaces.index(space):
            methods["send"](info["address"],player.getName()+" was already at "+space.get_name())
        else:
            methods["send"](info["address"],player.getName()+" moved to "+space.get_name())
            player.setPosition(board_spaces.index(space))

    def land_unowned_property(self,methods,info,player,space):
        methods["send"](info['address'],space.get_name()+" is unowned and may be"+\
        " bought for "+str(space.price)+". Enter '.monopoly buy' if you "+\
        "want to to buy it or '.monopoly pass' if not"
        Plugin.roll_req = False
        Plugin.buy_req = True
        #methods["send"](info["address"],getInfo(new_location))
        #something like the line above should be executed to give the user an idea
        #about what they are buying and the rest of their situation
        #such as ownership of other properties in that set and how much money they have

    def pay(self,methods,info,payer,receiver,amount):
        payer_alive = payer.reducePot(amount)
        receiver.increasePot(amount)

        if player_alive:
            methods["send"](info['address'],payer.getName+" now only has "+payer.getPot() +\
            "whereas "+receiver.getName()+" now has "+receiver.getPot()
            next_turn()

        else:
            methods["send"](info['address'],payer.getName+" is now out of the game "+\
            "whereas "+receiver.getName()+" now has "+receiver.getPot()
            Plugin.players.remove(player)
            next_turn()

    def offer_house(self,methods,info,player,property):
        num_prop_in_set = count_player_properties(player)[property.color]
        if num_prop_in_set == Property.set_houses[property.color]:
            cost_house = property.get_house_cost()
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

    """
    COMMUNITY CARD AND CHANCE METHODS
    """

    #all of these methods will take self,methods,info,player arguments for simplicity
    #additional arguments supplied can be found in the second element of the values of the dictionaries of the monopoly_assets.py file
    #here's an example
    #{"From sale of stock, you get $45":[0,(45)]}
    #0 refers to earn as it is the function at first index of community_deck_methods and (45) is the argument
    #additional arugments will be supplied using * so that they are split up

    def community_card(self,methods,info,player):
        #take community Card
        #must pick first in array, place it at back, and execute its function with correct args.
        community_card_methods = [earn,get_outta_jail,collect,go,jail,repairs,fine]
        methods["send"](info["address"],player.getName()+" is picking up a community card, it says:")
        card = community_deck.pop(0)#take first card, returns a dict {"message":[int,(tuple)]}
        card_string = next(iter(card))
        methods["send"](info["address"],card_string)
        #execute card: get function,add standard arguments,unpack those stored in the thing
        func = community_card_methods[card[card_string][0]]
        func(self,methods,info,player,*card[card_string][1])
        community_deck.append(card)#put it at the back

    def chance_card(self,methods,info,player):
        #chance_methods = [pay_all,reading_rail,boardwalk,go,railroad,get_outta_jail,jail,earn,illinois,fine,repairs,st_charles_place,util,move_back_three]
        chance_card_methods = [pay_all,reading_rail,move_to_property,go,railroad,get_outta_jail,jail,earn,fine,repairs,util,move_back_three]
        methods["send"](info["address"],player.getName()+" is picking up a chance card, it says:")
        card = chance_deck.pop(0)#take first card, returns a dict {"message":[int,(tuple)]}
        card_string = next(iter(card))
        methods["send"](info["address"],card_string)
        #execute card: get function,add standard arguments,unpack those stored in the thing
        func = community_card_methods[card[card_string][0]]
        func(self,methods,info,player,*card[card_string][1])
        chance_deck.append(card)#put it at the back

    def earn(self,methods,info,player,amount):
        player.increasePot(amount)
        methods["send"](info["address"],player.getName()+" now has a pot of "+player.getPot())
        next_turn()

    def get_outta_jail(self,methods,info,player):
        if player.imprisoned:
            player.imprisoned = False
            player.prison_time = 0
            methods["send"](info["address"],player.getName()+" escaped the jail")
            next_turn()
        else:
            player.get_outta_jail_card = True
            next_turn()

    def collect(self,methods,info,player,amount):
        for opponent in Plugin.players:#will iterate over player as well
            if player != opponent:
                pay(self,methods,info,opponent,player,amount)
        next_turn()

    def go(self,methods,info,player):
        player.setPosition(0)
        player.increasePot(200)
        next_turn()

    def jail(self,methods,info,player):
        if player.get_outta_jail_card:
            methods["send"](info["address"],player.getName()+" used his get out of jail free card!")
            player.setPosition(10)
            next_turn()
        else:
            player.setPosition(10)
            player.imprisoned = True
            next_turn()

    def fine(self,methods,info,player,amount):
        #must do this tomorrow
        player_alive = player.reducePot(amount)

        if player_alive:
            methods["send"](info["address"],player.getName+" was forced to pay "+\
            +str(amount)+" and now has "+player.getPot())
        else:
            methods["send"](info["address"],player.getName+" was forced to pay "+\
            +str(amount)+" on and now has no more money so has left the game")
            Plugin.players.remove(player)
        next_turn()

    def repairs(self,methods,info,player,house_fee,hotel_fee):
        property_list = [asset for asset in player.getPortfolio() if isinstance(asset,Property)]
        hotel_total = 0
        house_total = 0
        for property in property_list:
            if property.house_count == 5:
                hotel_total += 1
            else:
                house_total += property.house_count

        cost = house_fee * house_total + hotel_fee * hotel_total
        fine(self,methods,info,player,cost)

    def pay_all(self,methods,info,player,amount):
        other_players = [opponent for opponent in Plugin.players if opponent != player]
        total_amount = amount * len(other_players)
        player_alive = player.reducePot(total_amount)

        if player_alive:
            methods["send"](info["address"],player.getName+" was forced to pay "+\
            +str(amount)+" and now has "+player.getPot())
        else:
            methods["send"](info["address"],player.getName+" was forced to pay "+\
            +str(amount)+" on repairs and now has no more money so has left the game")
            Plugin.players.remove(player)

        for opponent in other_players:
            opponent.increasePot(amount)
        next_turn()

    def reading_rail(self,methods,info,player):
        reading_rail = board_spaces[5]
        move_to_space(self,methods, info, player,reading_rail)
        owner_info = find_owner("Reading Railroad")
        if owner_info[0]:
            #owned
            if owner_info[1] == player:
                methods["send"](info["address"],"You own Reading Railroad, but "+\
                "can not buy a house as railroads do not have houses!")
                next_turn()
            else:
                owner_railroads = count_player_properties(owner_info[1])["Railroad"]
                rent = reading_rail.rents[owner_railroads]
                methods["send"](info["address"],"Reading Railroad is owned by"+\
                owner_info[1].getName() + " and so "+player.getName()+" must pay them "+str(rent))
                pay(self,methods,info,player,owner_info[1],rent)
        else:
            #unowned
            land_unowned_property(self,methods,info,player,reading_rail)

    def railroad(self,methods,info,player):
        #find railroad, all railroads have index ending in five. in addition, player must move forwards.
        #if already at railroad must still go forward to next one
        for i in range(10): #player can only be 10 away from next railroad
            updatePosition(1)
            if is_instance(board_spaces[player.getPosition()],Railroad):
                break
        railroad = board_spaces[player.getPosition()]
        owner_info = find_owner(railroad.get_name())
        if owner_info[0]:
            if owner_info[1] == player:
                methods["send"](info["address"],player.getName()+" is at "+\
                railroad.get_name()+" which they already own")
                next_turn()
            else:
                owner_railroads = count_player_properties(owner_info[1])["Railroad"]
                rent = railroad.rents[owner_railroads]
                rent *= 2
                methods["send"](info["address"],railroad.get_name()+" is owned by"+\
                owner_info[1].getName() + " and so "+player.getName()+" must pay them "+str(rent))
                pay(self,methods,info,player,owner_info[1],rent)
        else:
            land_unowned_property(self,methods,info,player,railroad)

    def move_to_property(self,methods,info,player,property):
        move_to_space(self,methods, info, player,property)
        owner_info = find_owner(property.get_name())
        if owner_info[0]:
            if owner_info[1] == player:
                offer_house(self,methods,info,player,property)
            else:
                rent = property.rents[property.house_count]
                methods["send"](info["address"],property.get_name()+" is owned by"+\
                owner_info[1].getName() + " and so "+player.getName()+" must pay them "+str(rent))
                pay(self,methods,info,player,owner_info[1],rent)
        else:
            land_unowned_property(self,methods,info,player,boardwalk_space)

    def util(self,methods,info,player):
        start = False #make sure the user advances at least one pace
        while (not isinstance(board_spaces[player.getPosition()]),Utility) and start:
            start = True
            player.updatePosition(1)
        utility = board_spaces[player.getPosition()]
        owner_info = find_owner(utility.get_name())
        if owner_info[0]:
            if owner_info[1] == player:
                methods["send"](info["address"],player.getName()+" has landed on his own utility.")
                next_turn()
            else:
                methods["send"](info["address"],player.getName()+" has landed on "+\
                owner_info[0].getName()"'s utility and must pay ten times whatever he rolls now with two dice!")
                total = random.randint(1,6) + random.randint(1,6)
                methods[send](info["address"],player.getName()+" rolled a total of "+str(total))
                pay(self,methods,info,player,owner_info[1],total*10)
        else:
            land_unowned_property(self,methods,info,player,utility)

    def move_back_three(self,methods,info,player):
        if player.getPosition == 22:
            move_to_property(self,methods,info,player,board_spaces[19])
        elif player.getPosition == 26:
            #pick community card
        elif player.getPosition == 7:
            #send a message about being fined
            fine(self,methods,info,player,100)


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
        if Plugin.stage == 0 and Plugin.start_join_req:
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
            random.shuffle(community_deck)
            random.shuffle(chance_deck)
        else:
            methods["send"](info["address"],"This command is currently not possible")


    def roll(self,methods,info):
        player = Plugin.players[turn]
        if not player.imprisoned or player.prison_time == 2:
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)
            if player.prison_time == 2 and player.imprisoned:
                methods["send"](info["address"],"You are in prison, this is your last "+\
                "chance to leave for free by rolling a double".)
                if roll1 == roll2:
                    player.imprisoned = False
                    player.prison_time = 0
                    methods["send"](info["address"],"You rolled a "+str(roll1)+" twice and so are free!")
                else:
                    methods["send"](info["address"],"You did not roll a double so have to pay a fee to leave!")
                    fine(self,methods,info,player,50)

            move_amount = roll1 + roll2
            passed_go = player.updatePosition(move_amount)
            new_location = board_spaces[player.getPosition()]
            methods["send"](info['address'],player.getName()+" rolled "+str(move_amount) +\
            " and is now located at "+new_location.get_name())
            new_location_owned = find_owner(new_location.get_name())
            if new_location_owned[0]:##if property is owned by somebody
                owner = Plugin.players[new_location_owned[1]]

                if player == owner:
                    ##buy a house option

                    if isinstance(new_location,Property):
                        offer_house(self,methods,info,player,new_location)
                    else:
                        methods["send"](info["address"],"You have landed on your own property "+\
                        "but you cannot buy houses for railroads or utilities")
                        next_turn()

                else:
                    rent = get_rent(self,new_location,owner,move_amount)
                    methods["send"](info['address'],player.getName()+" landed on a property owned by "+\
                    owner.getName()+" and must pay them "+str(rent))
                    pay(self,methods,info,player,owner,rent)

            elif isinstance(new_location,Property) or isinstance(new_location,Utility) or isinstance(new_location,Railroad):
                #buy
                land_unowned_property(self,methods,info,player,new_location)

            elif player.getPosition() == 2 or player.getPosition() == 17 or player.getPosition() == 33:
                community_card(self,methods,info,player)

            elif player.getPosition() == 7 or player.getPosition() == 22 or player.getPosition() == 36:
                chance_card(self,methods,info,player)

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
                fine(self,methods,info,player,100)
                next_turn()

            elif player.getPosition == 4:
                fine(self,methods,info,player,100)
                next_turn()

            else:
                next_turn()
        else:
            methods["send"](info["address"],"you are in jail and will not move unless you roll a double!")
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)
            if roll1 == roll2:
                move_amount = roll1 + roll2
                passed_go = player.updatePosition(move_amount)
                new_location = board_spaces[player.getPosition()]
                methods["send"](info['address'],player.getName()+" rolled "+str(move_amount) +\
                " and is now located at "+new_location.get_name())
                new_location_owned = find_owner(new_location.get_name())
                if new_location_owned[0]:##if property is owned by somebody
                    owner = Plugin.players[new_location_owned[1]]
                    if player == owner:
                        ##buy a house option
                        if isinstance(new_location,Property):
                            offer_house(self,methods,info,player,new_location)
                        else:
                            methods["send"](info["address"],"You have landed on your own property "+\
                            "but you cannot buy houses for railroads or utilities")
                            next_turn()
                    else:
                        rent = get_rent(self,new_location,owner,move_amount)
                        methods["send"](info['address'],player.getName()+" landed on a property owned by "+\
                        owner.getName()+" and must pay them "+str(rent))
                        pay(self,methods,info,player,owner,rent)

                elif isinstance(new_location,Property) or isinstance(new_location,Utility) or isinstance(new_location,Railroad):
                    #buy
                    land_unowned_property(self,methods,info,player,new_location)

                elif player.getPosition() == 22:
                    chance_card(self,methods,info,player)

                else:#don't need to check other options as we know user starts at index ten and throwing a double limits the possibilities
                    next_turn()

            else:
                self.prison_time += 1
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
