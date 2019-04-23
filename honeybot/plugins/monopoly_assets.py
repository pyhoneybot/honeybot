# Game Objects
class Space(object):
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

class Property(Space):
    set_houses = {
                  "Violet":2,
                  "Light blue":3,
                  "Purple":3,
                  "Orange":3,
                  "Red":3,
                  "Yellow":3,
                  "Green":3,
                  "Blue":2
                  }

    def __init__(self, name, color, price,
                 rent, one_house_rent, two_house_rent,
                 three_house_rent, four_house_rent, hotel_rent,
                 house_cost):
        super(Property,self).__init__(name)
        self.price = price
        self.color = color
        self.house_count = 0 #5 means hotel
        self.rents = {0:rent,
                      1:one_house_rent,
                      2:two_house_rent,
                      3:three_house_rent,
                      4:four_house_rent,
                      5:hotel_rent}
        self.house_cost = house_cost

    def get_house_cost(self):
        return self.house_cost

    def info(self):
        information = [
                       self.name+" is a "+self.color+" property that costs "+str(self.price)+".",
                       "It currently has "+str(self.house_count)+" houses.",
                       "With no houses rent is "+str(self.rents[0])+".",
                       "With 1 house rent is "+str(self.rents[1])+".",
                       "With 2 houses rent is "+str(self.rents[2])+".",
                       "With 3 houses rent is "+str(self.rents[3])+".",
                       "With 4 houses rent is "+str(self.rents[4])+".",
                       "With a hotel rent is "+str(self.rents[5])+".",
                       "A house costs "+str(self.house_cost)+" to build."
        ]
        return " ".join(information)


class Railroad(Space):
    def __init__(self,name):
        super(Railroad, self).__init__(name)
        self.price = 200
        self.rents = {1:25,
                      2:50,
                      3:100,
                      4:200}

    def info(self):
        information = [
                       self.name+" is a railroad that costs "+str(self.price)+".",
                       "If a player has one railroad only the rent is "+str(self.rents[1])+".",
                       "If a player has two railroads the rent is "+str(self.rents[2])+".",
                       "If a player has three railroads only the rent is "+str(self.rents[3])+".",
                       "If a player has four railroads only the rent is "+str(self.rents[4])+"."
                       ]
        return " ".join(information)


class Utility(Space):
    def __init__(self,name):
        super(Utility,self).__init__(name)
        self.price = 150
        self.rents = {1:"4 *",
                      2:"10 *"}

    def info(self):
        return self.name+" is a utility that costs "+str(self.price)+". If you have " +\
        "one utility rent is four times the amount the player rolled on the dice or "+\
        "if you have two utilities the rent is ten times!"

board_spaces = [
                Space("GO"),
                Property("Mediterranean Ave.","Violet",60,2,10,30,90,160,250,50),
                Space("Community Card"),
                Property("Baltic Ave.","Violet",60,4,20,60,180,320,450,50),
                Space(" Tax"),
                Railroad("Reading Railroad"),
                Property("Oriental Ave.","Light blue",100,6,30,90,270,400,550,50),
                Space("Chance Card"),
                Property("Vermont Ave.","Light blue",100,6,30,90,270,400,550,50),
                Property("Conneticut Ave.","Light blue",120,8,40,100,300,450,600,50),
                Space("Jail"),
                Property("St. Charles Pl.","Purple",140,10,50,150,450,625,750,100),
                Utility("Electric Company"),
                Property("States Ave.","Purple",140,10,50,150,450,625,750,100),
                Property("Virginia Ave.","Purple",160,12,60,180,500,700,900,100),
                Railroad("Pennsylvania Railroad"),
                Property("St. James Pl.","Orange",180,14,70,200,550,750,950,100),
                Space("Community Card"),
                Property("Tennessee Ave.","Orange",180,14,70,200,550,750,950,100),
                Property("New York Ave.","Orange",200,16,80,220,600,800,1000,100),
                Space("Free Parking"),
                Property("Kentucky Ave.","Red",220,18,90,250,700,875,1050,150),
                Space("Chance Card"),
                Property("Indiana Ave.","Red",220,18,90,250,700,875,1050,150),
                Property("Illinois Ave.","Red",240,20,100,300,750,925,1100,150),
                Railroad("B. & O. Railroad"),
                Property("Atlantic Ave.","Yellow",260,22,110,330,800,975,1150,150),
                Property("Ventnor Ave.","Yellow",260,22,110,330,800,975,1150,150),
                Utility("Water Works"),
                Property("Marvin Gardens","Yellow",280,24,120,360,850,1025,1200,150),
                Space("Go to Jail"),
                Property("Pacific Ave.","Green",300,26,130,390,900,1100,1275,200),
                Property("No. Carolina Ave.","Green",300,26,130,390,900,1100,1275,200),
                Space("Community Card"),
                Property("Pennsylvania Ave.","Green",320,28,150,450,1000,1200,1400,200),
                Railroad("Short Line Railroad"),
                Space("Chance Card"),
                Property("Park Place","Blue",350,35,175,500,1100,1300,1500,200),
                Space("Luxury Tax"),
                Property("Boardwalk","Blue",400,50,200,600,1400,1700,2000,200)
               ]

#chance_methods = [pay_all,reading_rail,move_to,go,railroad,get_outta_jail,jail,earn,fine,repairs,util,move_back_three]
#in the following decks, the second value of the dictionaries in the array must be an iterable and not an int,
#hence why you will see things like (50,) so that python keeps it as a tuple
chance_deck = [
               {"You have been elected chairman of the board, pay each player $50":[0,(50,)]},
               {"Take a ride on the reading, if you pass GO collect $200":[1,()]},
               {"Take a walk on the board walk, advance token to board walk":[2,(board_spaces[39],)]},
               {"Advance to go, collect $200":[3,()]},
               {"Advance token to the nearest Railroad and pay owner Twice the Rental owed. If Railroad is unowned you may buy it from the bank":[4,()]},
               {"Advance token to the nearest Railroad and pay owner Twice the Rental owed. If Railroad is unowned you may buy it from the bank":[4,()]},
               {"Get out of jail free. This card may be kept until needed or sold":[5,()]},
               {"Go directly to jail. Do not pass Go, do not collect $200":[6,()]},
               {"Bank pays you dividend of $50":[7,(50,)]},
               {"Advance to Illinois Ave":[2,(board_spaces[24],)]},
               {"Pay poor tax of $15":[8,(15,)]},
               {"Make general repairs on all your property. For each house pay $25, for each hotel $100":[9,(25,100)]},
               {"Advance to St. Charles Place. If you pass Go, collect $200":[2,(board_spaces[11],)]},
               {"Your building and loan matures. Collect $150":[7,(150,)]},
               {"Advance token to nearest utility. If Unowned you may buy it from the bank. If owned throw dice and pay owner ten times the amount thrown.":[10,()]},
               {"Go back 3 spaces":[11,()]}
              ]

#cc methods = [earn,get_outta_jail,collect,go,jail,repairs,fine]
community_deck = [
                  {"Get out of jail free.":[1,()]},
                  {"From sale of stock, you get $45":[0,(45,)]},
                  {"Grand opera opening. Collect $50 from every player for opening night seats":[2,(50,)]},
                  {"Advance to Go, collect $200":[3,()]},
                  {"Xmas fund matures, collect $100":[0,(100,)]},
                  {"Go directly to jail. Do not pass Go. Do not collect $200":[4,()]},
                  {"Life insurance matures, collect $200":[0,(200,)]},
                  {"You are assessed for street repairs. $40 per house, $115 per hotel":[5,(40,115)]},
                  {"Pay hospital $100":[6,(100,)]},
                  {"Income tax refund, collect $20":[0,(20,)]},
                  {"Doctor's fee, pay $50":[6,(50,)]},
                  {"You inherit $100":[0,(100,)]},
                  {"Pay school tax of $150":[6,(150,)]},
                  {"Receive for services $25":[0,(25,)]},
                  {"Bank error in your favor, collect $200":[0,(200,)]},
                  {"You have won second prize in a beauty contest, collect $10":[0,(10,)]}
                 ]
