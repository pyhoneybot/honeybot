# -*- coding: utf-8 -*-
"""
[hangman.py]
Hangman Game Plugin

[Author]
Justin Walker

[About]
Plays game of hangman

[Commands]
>>> .hangman start
Starts hangman game and returns game screen.

>>> .hangman guess <<word or letter>>
Submits word or letter guess and returns game screen.
"""

import random


class Plugin:
    def __init__(self):
        pass

# __hangman allows the plugin to call the hangman class and sends input to the
# game. Detects which command is entered, either 'start' or 'guess', and if
# guess is followed by a single char or entire word. Error displayed upon
# incorrect command.

    def hangman(self, command, word):
        msg = "Command entered incorrectly."
        if command.lower() == "start":
            self.class_hangman = Hangman()
            msg = "Welcome to hangman! " + \
                  "You may use command 'start' to start new game  " + \
                  "or 'guess ---' with a word or letter to play." + \
            self.class_hangman.display_screen()
        elif command.lower() == "guess":
            if len(word.strip()) > 1:
                self.class_hangman.guess_word(word)
                msg = self.class_hangman.display_screen()
            elif len(word.strip()) == 1:
                self.class_hangman.guess_letter(word)
                msg = self.class_hangman.display_screen()
        return msg

    def run(self, incoming, methods, info, bot_info):
            try:
                msgs = info['args'][1:][0].split()
                if info['command'] == 'PRIVMSG':
                    if len(msgs) > 1:
                        if msgs[0] == '.hangman':
                            command = msgs[1]
                            word = ""
                            if len(msgs) > 2:
                                word = msgs[2]
                            methods['send'](
                                    info['address'], \
                                    Plugin.hangman(self, command, word))
            except Exception as e:
                print('woops plugin error', e)


class Hangman:
    def __init__(self):
        self.wordChoices = [
            "pig", "candy", "nerve", "shocking", "eating", "werewolf",
            "blouse", "bloom", "coward", "crafty", "doctor", "container",
            "cursed", "convertible", "beaver", "biblical", "arsonist",
            "victory", "loneliness", "blowgun", "spider", "federal",
            "analysis", "reverse", "horizontal", "martini", "bleeder",
            "ammonia", "biplane", "bless", "crusher", "hippo", "americana",
            "ambient", "blinking", "vibrator", "apocalypse", "appetite",
            "baptism", "calculation", "knuckle", "formula", "robbery",
            "basement", "decadence", "fright", "jigsaw", "guidebook",
            "robotic", "arrogant", "acrobat", "weasel", "blueberry",
            "anybody", "propeller", "wolves", "crystal", "flamethrower",
            "breakwater", "discontent", "creation", "academic", "downfall",
            "peach", "cunning", "atonement", "tongue", "academy", "vaccant",
            "family", "brave", "adaptive", "insane", "crayon", "healing",
            "ghoul", "abandon", "robotic", "plasma", "hidden"
        ]
        randIndex = random.randint(0,len(self.wordChoices)-1)
        self.gameWord = self.wordChoices[randIndex]
        print(self.gameWord)
        self.display = "-"*len(self.gameWord)
        self.guessCount = len(self.display) + 3
        self.display_message = " You have {0} guesses remaining." \
                               .format(self.guessCount)
        self.endGame = False
        self.endMessage = "You shouldn't be able to see this."

# guess_letter is used when user enters a single character guess.

    def guess_letter(self, guessLetter):
    # First find at which indeces the guessed letter is in the word.

        indeces = []
        index = 0
        newWord = ""
        for letter in self.gameWord:
            if guessLetter.lower() == letter:
                indeces.append(index)
            index += 1

    # Form new word with - for incorrect letter and add in correct letter
    # at found indeces

        for tracker in range(len(self.display)):
            if len(indeces)>0 and indeces[0] == tracker:
                indeces.pop(0)
                newWord += guessLetter
            elif self.display[tracker] != "-":
                newWord += self.display[tracker]
            else: 
                newWord += "-"

        self.display = newWord
        self.check_win()

# guess_word is for when user tries to guess the complete word.

    def guess_word(self, wordGuess):
        if wordGuess.lower() == self.gameWord:
            self.display = self.gameWord
            self.check_win()
        else:
            self.display_message = "'{0}' was incorrect. " \
                                   .format(wordGuess) + \
                                   "You have {1} guesses remaining." \
                                   .format(wordGuess,self.guessCount)

# check_win determines if the user has guessed the entire word after each
# guess. If the user hasn't won, they lost one of their guesses.

    def check_win(self):
        win = True
        for letter in self.display:
            if letter == "-":
                win = False

        if win == True:
            self.display = "'{0}' is correct. You win!".format(self.gameWord)
            self.display_message = " You had {0} guesses remaining." \
                                   .format(self.guessCount) + \
                                   "\nUse 'start' command to try again."
            self.endGame = True
            self.endMessage = self.display+self.display_message
        else:
            self.decrement_guesses()

# decrement_guesses reduces the players guessCount and declares loss if the
# count reaches 0.

    def decrement_guesses(self):
        self.guessCount -= 1
        if self.guessCount == 0:
            self.endMessage = "You have no more guesses.\n" + \
                           "The correct word was '{0}'.\n" \
                           .format(self.gameWord) + \
                           "You lose. Use start command to try again"
            self.endGame = True
        else:
            self.display_message = " You have {0} guesses remaining." \
                                   .format(self.guessCount)

# display_screen is to output what the user should see in the game's current
# state.

    def display_screen(self):
        if self.endGame == False:
            return self.display + self.display_message
        else:
            return self.endMessage
            

def send(info, message):
    print(message)


def test_them(plugin, msg):

    methods = {"send":send}
    msg = msg
    info = {'args':[None,msg],
            'command':'PRIVMSG',
            'address':'That place'}
    plug.run("",methods,info)