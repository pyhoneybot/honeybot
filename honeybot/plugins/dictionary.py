# -*- coding: utf-8 -*-
"""
[dictionary.py]
Dictionary Plugin

[Author]
Nishant, JPMorgan Chase & Co.

[About]
sends the meaning of the word
requires PyDictionary to be installed
can use pip -> "pip install PyDictionary"

[Commands]
>>> .dictionary <<word>>
returns meaning of the word specified
"""

from PyDictionary import PyDictionary

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()

            if info['command'] == 'PRIVMSG' and msgs[0] == '.dictionary':
                dict = PyDictionary()
                word = str(msgs[1])
                defin = dict.meaning(word)['Noun']
                methods['send'](info['address'], '{}'.format(defin))
        except Exception as e:
            print('woops plug', e)
