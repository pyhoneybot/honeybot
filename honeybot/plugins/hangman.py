# -*- coding: utf-8 -*-
"""
[hangman.py]
Hangman Game Plugin

[Author]
Justin Walker

[About]
Plays game of hangman

[Commands]
>>> .selfTrivia
returns a random question
Currently working on adding multiple choice and a timer reveal.
"""

class Plugin:
    def __init__(self):
        pass

    def __hangman(word):
        if word.lowercase() == "start" 

    def run(self, incoming, methods, info):
            try:
                msgs = info['args'][1:][0].split()
                if info['command'] == 'PRIVMSG':
                    if len(msgs) > 1:
                        if msgs[0] == '.dictionary':
                            word = msgs[1]
                            methods['send'](info['address'], Plugin.__dictionary(self, word))
            excpet Exception as e:
                print('woops plugin error', e)