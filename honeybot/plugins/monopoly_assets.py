# Game Objects
class Property:
    def __init__(self, name, color, price,
                 rent, one_house_rent, two_house_rent,
                 three_house_rent, four_house_rent, hotel_rent,
                 build_cost):
        self.name = name
        self.color = color
        self.price = price
        self.rents = {"one":one_house_rent,
                      "two":two_house_rent,
                      "three":three_house_rent,
                      "four":four_house_rent,
                      "hotel":hotel_rent}
        self.build_cost = build_cost


class Railroad:
    def __init__(self, name):
        self.name = name
        self.price = 200
        self.rents = {"one_railroad":25,
                      "two_railroad":50,
                      "three_railroad":100,
                      "four_railroad":200}


class Utility:
    def __init__(self, name):
        self.name = name
        self.price = 150
        self.rents = {"one_utility":"4x"
                      "two_utility":"10x"}


# Assets
currencies = [1,5,10,20,50,100,500]

board_spaces = {
        1:"GO",
        2:Property("Mediterranean Ave.","Violet",60,2,10,30,90,160,250,50),
        3:"Draw Community Card",
        4:Property("Baltic Ave.","Violet",60,4,20,60,180,320,450,50),
        5:"Income Tax",
        6:Railroad("Reading Railroad"),
        7:Property("Oriental Ave.","Light blue",100,6,30,90,270,400,550,50),
        8:"Draw Chance Card",
        9:Property("Vermont Ave.","Light blue",100,6,30,90,270,400,550,50),
        10:Property("Connecticut Ave.","Light blue",120,8,40,100,300,450,600,50),
        11:"Jail",
        12:Property("St. Charles Pl.","Purple",140,10,50,150,450,625,750,100),
        13:Utility("Electric Company"),
        14:Property("States Ave.","Purple",140,10,50,150,450,625,750,100),
        15:Property("Virginia Ave.","Purple",160,12,60,180,500,700,900,100),
        16:Railroad("Pennsylvania Railroad"),
        17:Property("St. James Pl.","Orange",180,14,70,200,550,750,950,100),
        18:"Draw Community Card",
        19:Property("Tennessee Ave.","Orange",180,14,70,200,550,750,950,100),
        20:Property("New York Ave.","Orange",200,16,80,220,600,800,1000,100),
        21:"Free Parking",
        22:Property("Kentucky Ave.","Red",220,18,90,250,700,875,1050,150),
        23:"Draw Chance Card",
        24:Property("Indiana Ave.","Red",220,18,90,250,700,875,1050,150),
        25:Property("Illinois Ave.","Red",240,20,100,300,750,925,1100,150),
        26:Railroad("B. & O. Railroad"),
        27:Property("Atlantic Ave.","Yellow",260,22,110,330,800,975,1150,150),
        28:Property("Ventnor Ave.","Yellow",260,22,110,330,800,975,1150,150),
        29:Utility("Water Works"),
        30:Property("Marvin Gardens","Yellow",280,24,120,360,850,1025,1200,150),
        31:"Go to Jail",
        32:Property("Pacific Ave.","Green",300,26,130,390,900,1100,1275,200),
        33:Property("No. Carolina Ave.","Green",300,26,130,390,900,1100,1275,200),
        34:"Draw Community Card",
        35:Property("Pennsylvania Ave.","Green",320,28,150,450,1000,1200,1400,200),
        36:Railroad("Short Line Railroad"),
        37:"Draw Chance Card",
        38:Property("Park Place","Blue",350,35,175,500,1100,1300,1500,200),
        39:"Luxury Tax",
        40:Property("Boardwalk","Blue",400,50,200,600,1400,1700,2000,200)
}

game_board = [
    [ [11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21] ],
    [ [10],                                             [22] ],
    [ [ 9],                                             [23] ],
    [ [ 8],                                             [24] ],
    [ [ 7],                                             [25] ],
    [ [ 6],                                             [26] ],
    [ [ 5],                                             [27] ],
    [ [ 4],                                             [28] ],
    [ [ 3],                                             [29] ],
    [ [ 2],                                             [30] ],
    [ [ 1],[40],[39],[38],[37],[36],[35],[34],[33],[32],[31] ]
]

chance_deck = {
        1:"You have been elected chairman of the board, pay each player $50",
        2:"Take a ride on the reading, if you pass GO collect $200",
        3:"Take a walk on the board walk, advance token to board walk",
        4:"Advance to go, collect $200",
        5:"Advance token to the nearest Railroad and pay owner Twice the " +
         " Rental owed. If Railroad is unowned you may buy it from the bank",
        6:"Advance token to the nearest Railroad and pay owner Twice the" +
         " Rental owed. If Railroad is unowned you may buy it from the bank",
        7:"Get out of jail free. This card may be kept until needed or sold",
        8:"Go directly to jail. Do not pass Go, do not collect $200",
        9:"Bank pays you dividend of $50",
        10:"Advance to Illinois Ave",
        11:"Pay poor tax of $15",
        12:"Make general repairs on all your property. For each house pay " +
         "$25, for each hotel $100",
        13:"Advance to St. Charles Place. If you pass Go, collect $200",
        14:"Your building and loan matures. Collect $150",
        15:"Advance token to nearest utility. If Unowned you may buy it " +
         "from the bank. If owned throw dice and pay owner ten times the " +
         "amount thrown",
        16:"Go back 3 spaces"
}

community_deck = {
        1:"Get out of jail free. This card may be kept until needed or sold",
        2:"From sale of stock, you get $45",
        3:"Grand opera opening." +
         "Collect $50 from every player for opening night seats",
        4:"Advance to Go, collect $200",
        5:"Xmas fund matures, collect $100",
        6:"Go directly to jail. Do not pass Go. Do not collect $200",
        7:"Life insurance matures, collect $200",
        8:"You are assessed for street repairs. $40 per house," +
         "$115 per hotel",
        9:"Pay hospital $100",
        10:"Income tax refund, collect $20",
        11:"Doctor's fee, pay $50",
        12:"You inherit $100",
        13:"Pay school tax of $150",
        14:"Receive for services $25",
        15:"Bank error in your favor, collect $200",
        16:"You have won second prize in a beauty contest, collect $10"
}
