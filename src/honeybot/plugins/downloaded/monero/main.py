# -*- coding: utf-8 -*-
"""
[monero.py]
Monero Price Checking Plugin

[Author]
A. Eigenbrot


[About]
Checks the current price for Monero via the cryptocompare.com API

[Commands]
>>> .xmr [currency]
returns current value of Monero in the currency specified (default is USD).
Currency must be a 3-letter capital string.
Examples: USD, EUR, BTC, GBP
"""

import json

from requests import Session


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".xmr":
                try:
                    currency = msgs[1].upper()
                except IndexError:
                    currency = "USD"

                api_url = "https://min-api.cryptocompare.com/data/price"
                params = {"fsym": "XMR", "tsyms": currency}

                session = Session()
                headers = {"Accepts": "application/json"}
                session.headers.update(headers)

                result = session.get(api_url, params=params)
                data = json.loads(result.text)
                methods["send"](
                    info["address"], "{} {}".format(data[currency], currency)
                )

        except Exception as e:
            print("woops! monero plugin error:", e)
