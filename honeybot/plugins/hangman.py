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
        pass

    def start(self):
        pass

    def guess_letter(self, guessLetter):
        pass

    def guess_word(self, wordGuess):
        pass

    def check_win(self):
        pass

    def decrement_guesses(self):
        pass

    def display_screen(self):
        pass