# -*- coding: utf-8 -*-
"""
[monero.py]
Monero Price Checking Plugin

[Author]
A. Eigenbrot


[About]
Checks the current price for Monero via the cryptocompare.com API

[Commands]
>>> .xmr
returns current value of Monero in USD
"""

from requests import Session
import json

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.xmr':
                api_url = "https://min-api.cryptocompare.com/data/price"
                params = {'fsym': 'XMR', 'tsyms': 'USD'}

                session = Session()
                headers = {'Accepts': 'application/json'}
                session.headers.update(headers)

                result = session.get(api_url, params=params)
                data = json.loads(result.text)
                methods['send'](info['address'], '{:.2f} USD'.format(data['USD']))

        except Exception as e:
            print('woops! monero plugin error:', e)
