"""
[pynews.py]
Python news checking plugin

[Author]
Sam Deans

[Github]
@sdeans0

[About]
Finds the top five news items on python.org and prints them to the IRC

[Commands]
>>> .pynews
returns the top 5 python.org news articles
"""

import requests
from bs4 import BeautifulSoup


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1] == ".pynews":
                # Get python website
                response = requests.get("https://www.python.org")
                html = BeautifulSoup(response.text)
                # The news section is the first <div class='shrubbery'> in the page
                # So get all the links in that section
                news_links = (
                    html.find("div", class_="shrubbery").find("ul", class_="menu").find_all("a")
                )
                # Iterate through the links, send each one to the chat with its
                # associated title (a.contents[0])
                for a in news_links:
                    methods["send"](info["address"], ": ".join([a.contents[0], a["href"]]))
        except Exception as e:
            print("woops plugin", __file__, e)
