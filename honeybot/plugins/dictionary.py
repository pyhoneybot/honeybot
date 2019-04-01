# -*- coding: utf-8 -*-
"""
[dictionary.py]
Dictionary Plugin

[Author]
Nishant, JPMorgan Chase & Co.

[About]
sends the meaning of the word

[Commands]
>>> .dictionary <<word>>
returns meaning of the word specified
"""

import PyDictionary


class Plugin:
    def __init__(self):
        pass

    def __dictionary(self, word):
        return PyDictionary().meaning(word).get('Noun')

    def run(self, incoming, methods, info):
        try:
            # if '!~' in info['prefix']:
            # print(info)
            msgs = info['args'][1:][0].split()
            if info['command'] == 'PRIVMSG':
                if len(msgs) > 1:
                    if msgs[0] == '.dictionary':
                        word = msgs[1]
                        methods['send'](info['address'], Plugin.__dictionary(self, word))
        except Exception as e:
            print('woops plug', e)
