#player class

class Player:

    def __init__(self,name):
        #name will be the nickname in the IRC server
        #pot is the amount of money the player starts with
        #portfolio is an array with the indexes of the user's properties from the board spaces dict
        self.name = name
        self.pot = 1500
        self.portfolio = []

    def getName(self):
        return self.name

    def getPot(self):
        return str(self.pot)

    def increasePot(self,amount):
        self.pot += amount

    def reducePot(self,amount):
        self.pot -= amount

    def getPortfolio:
        return self.portfolio
