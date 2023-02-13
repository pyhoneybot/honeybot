"""
[bitcoin.py]
Bitcoin Price Checking Plugin

[Author]
Gabriele Ron

[Website]
https://Macr0Nerd.github.io

[About]
Checks the current price for Bitcoin through the Legacy Coin Market Cap API
TODO: Update API to new Coin Market Cap API

[Commands]
>>> .btc
returns current value of bitcoin
"""

import requests


class Plugin:
    def __init__(self):
        self.api_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            # msgs = info['args'][1:][0].split()

            if info["command"] == "PRIVMSG" and info["args"][1] == ".btc":
                response = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/")
                response_json = response.json()
                methods["send"](info["address"], "$" + response_json[0]["price_usd"])

        except Exception as e:
            print("woops plugin", __file__, e)
