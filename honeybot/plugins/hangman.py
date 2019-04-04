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
        pass

    def check_win(self):
        pass

    def decrement_guesses(self):
        pass

    def display_screen(self):
        pass