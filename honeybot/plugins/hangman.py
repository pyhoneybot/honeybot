# -*- coding: utf-8 -*-
"""
[hangman.py]
Hangman Game Plugin

[Author]
Justin Walker

[About]
Plays game of hangman

[Commands]
"""

class Plugin:
    def __init__(self):
        pass

    def __hangman(self, command):
        pass

    def run(self, incoming, methods, info):
            try:
                msgs = info['args'][1:][0].split()
                if info['command'] == 'PRIVMSG':
                    if len(msgs) > 1:
                        if msgs[0] == '.hangman':
                            word = msgs[1]
                            methods['send'](info['address'], Plugin.__hangman(self, command))
            except Exception as e:
                print('woops plugin error', e)

class Hangman:
    def __init__(self):
        self.wordChoices = ["pig"]

    def start(self):
        randIndex = random.randint(0,len(self.wordChoices)-1)
        self.gameWord = self.wordChoices[randIndex]
        self.display = "_"*len(self.gameWord)
        self.guessCount = len(self.display) + 3
        self.display_message = "You have {0} guesses remaining.".format(self.guessCount)

    def guess_letter(self, guessLetter):
        indeces = []
        index = 0
        newWord = ""

        for letter in self.gameWord:
            if guessLetter.lower() == letter:
                indeces.append(index)
            index += 1

        for tracker in range(len(self.display)):
            if len(indeces)>0 and indeces[0] == tracker:
                indeces.pop(0)
                newWord += guessLetter
            elif self.display[tracker] != "_":
                newWord += self.display[tracker]
            else: 
                newWord += "_"

        self.display = newWord
        self.check_win()

    def guess_word(self, wordGuess):
        if wordGuess.lower() == self.gameWord:
            self.display = self.gameWord
            self.check_win()
        else:
            self.display_message = "'{0}' was incorrect. You have {1} guesses remaining.".format(wordGuess,guessCount)

    def check_win(self):
        win = True
        for letter in self.display:
            if letter == "_":
                win = False

        if win == True:
            self.display = "'{0}' is correct. You win!".format(self.gameWord)
            self.display_message = " You had {0} guesses remaining.".format(self.guessCount)
        else:
            self.decrement_guesses()

    def decrement_guesses(self):
        self.guessCount -= 1
        if self.guessCount == 0:
            self.display = "You have no more guesses.\n" + \
                           "The correct word was '{0}'.\n".format(self.gameWord)
            self.display_message = "You lose."
        else:
            self.display_message = " You have {0} guesses remaining.".format(self.guessCount)

    def display_screen(self):
        return self.display + self.display_message