#player class

class Player:

    def __init__(self,name):
        #name will be the nickname in the IRC server
        #pot is the amount of money the player starts with
        #portfolio is an array with the indexes of the user's properties from the board spaces dict
        self.name = name
        self.pot = 1500
        self.portfolio = []
        self.position = 0
        self.imprisoned = False
        self.prison_time = 0
        self.get_outta_jail_card = False

    def updatePosition(self,amount):
        passed_go = False
        self.position += amount
        if self.position >= 39:
            passed_go = True
            self.position -= 40
            self.increasePot(200)
            if self.position > 39:
                self.position -= 40
        return passed_go

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def getPot(self):
        return str(self.pot)

    def increasePot(self,amount):
        self.pot += amount

    def reducePot(self,amount):
        if self.pot > amount:
            self.pot -= amount
            return True #they are still alive
        else:
            self.pot = 0
            return False #no longer alive

    def setPosition(self,index):
        #ensure index is between 0 and 39
        self.position = index

    def getPortfolio(self):
        return self.portfolio

    def checkWon():
        pass
