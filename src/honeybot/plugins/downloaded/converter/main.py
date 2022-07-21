"""
[converter.py]
Currency Converter Plugin

[Author]
Angelo Giacco

[About]
Converts currencies

[Commands]
>>> .convert <<base currency code>> <<target currency code>> <<amount>>
returns the conversion: amount argument is optional with a default of 1
.convert help
shows a list of currencies supported
"""
import requests
import math
from bs4 import BeautifulSoup


class Plugin:
    def __init__(self):
        pass

    currencies = [
        "GBP",
        "EUR",
        "USD",
        "ARS",
        "AUD",
        "BHD",
        "BWP",
        "BRL",
        "BND",
        "BGN",
        "CAD",
        "CLP",
        "CNY",
        "COP",
        "HRK",
        "CZK",
        "DKK",
        "HKD",
        "HUF",
        "ISK",
        "INR",
        "IDR",
        "IRR",
        "ILS",
        "JPY",
        "KZT",
        "KRW",
        "KWD",
        "LYD",
        "MYR",
        "MUR",
        "MXN",
        "NPR",
        "NZD",
        "NOK",
        "OMR",
        "PKR",
        "PHP",
        "PLN",
        "QAR",
        "RON",
        "RUB",
        "SAR",
        "SGD",
        "ZAR",
        "LKR",
        "SEK",
        "CHF",
        "TWD",
        "THB",
        "TTD",
        "TRY",
        "AED",
    ]

    def help(self, methods, info):
        methods["send"](info["address"], "showing supported currencies")
        currency_lists = [
            Plugin.currencies[5 * i: 5 * i + 5]
            for i in range(0, math.ceil(len(Plugin.currencies) / 5))
        ]
        for currency_list in currency_lists:
            methods["send"](info["address"], " ".join(currency_list))

    def conv(self, base_cur, target_cur, amount="1"):
        def is_number(char):
            try:
                float(char)
                return True
            except ValueError:
                return False

        base_cur = base_cur.upper()
        target_cur = target_cur.upper()
        if base_cur not in Plugin.currencies or target_cur not in Plugin.currencies:
            return "one of the currencies is invalid. " \
                   "enter .converter help to see supported currencies"
        elif not (is_number(amount)):
            return "invalid amount entered, it must be a number. default is 1"
        else:
            base_url = "https://www.x-rates.com/calculator/?"
            url = (
                base_url +
                "from=" +
                base_cur +
                "&to=" +
                target_cur +
                "&amount=" +
                str(amount)
            )
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")

            part1 = soup.find(class_="ccOutputTrail").previous_sibling
            part2 = soup.find(class_="ccOutputTrail").get_text(strip=True)
            converted = "{}{}".format(part1, part2)
            return str(amount) + base_cur + " is equal to " + converted + target_cur

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".convert":
                if len(msgs) == 3:
                    methods["send"](
                        info["address"], Plugin.conv(self, msgs[1], msgs[2])
                    )
                elif len(msgs) == 4:
                    methods["send"](
                        info["address"], Plugin.conv(self, msgs[1], msgs[2], msgs[3])
                    )
                elif len(msgs) == 2 and msgs[1] == "help":
                    methods["send"](info["address"], Plugin.help(self, methods, info))
                elif len(msgs) == 2 and msgs[1] != "help":
                    methods["send"](
                        info["address"],
                        "if only two arugments sent, second argument must be help",
                    )
                elif len(msgs) > 4:
                    methods["send"](info["address"], "too many arguments")
                    methods["send"](
                        info["address"], "either two currencies with an optional amount"
                    )
                    methods["send"](info["address"], "or help")
                elif len(msgs) == 1:
                    methods["send"](
                        info["address"], "converter plugin requires arguments:"
                    )
                    methods["send"](
                        info["address"], "either two currencies with an optional amount"
                    )
                    methods["send"](info["address"], "or help")
        except Exception as e:
            print("woops converter plugin error ", e)
