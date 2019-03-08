# -*- coding: utf-8 -*-
"""
[calc.py]
Caesar Cipher plugin

[Author]
Kyle Galloway

[About]
encrypts and decrypts using a caesar cipher
"""
import codecs


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()

            if info['command'] == 'PRIVMSG':
                if len(msgs) > 1:
                    if msgs[0] == '.caesar_cipher':
                        expr = msgs[1]
                        encoded = codecs.encode(expr, "rot-13")
                        print(encoded)
                        methods['send'](info['address'], '{}'.format(
                                encoded)
                        )
        except Exception as e:
            print('woops plugin', __file__, e)
