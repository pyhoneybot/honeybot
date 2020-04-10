# -*- coding: utf-8 -*-
"""
[pypi.py]
Pypi Search Plugin
[Author]
Donald Lieu
[About]
Searches for Python packages on pypi.org
[Commands]
>>> .pypi <search term>
returns first 3 result links
"""

import requests
from bs4 import BeautifulSoup


class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1][:5] == ".pypi":
                query_: str = info["args"][1][6:]
                payload = {"q": query_}
                url_: str = "https://pypi.org/search/"
                r = requests.get(url_, params=payload)
                soup = BeautifulSoup(r.content, "html.parser")
                # Return a max of 3 results
                num_results = soup.find("strong").get_text()
                # Format string
                if num_results[-1] == "+":
                    num_results = num_results[:-1]
                num_results = int(num_results.replace(",", ""))
                if num_results > 3:
                    num_results = 3
                elif num_results == 0:
                    methods["send"](info["address"], "No results")
                links = soup.find_all("a")
                for i in range(num_results):
                    methods["send"](
                        info["address"], "https://pypi.org" + links[7 + i]["href"]
                    )
        except Exception as e:
            print("woops plugin error ", e)
