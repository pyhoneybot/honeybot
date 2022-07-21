"""
[news.py]
Greet Plugin

[Author]
Angelo Giacco

[About]
Gets the top 10 headlines around the world from bbc world news

[Commands]
>>> .news
returns string of ten news headlines with newlines between
"""
from bs4 import BeautifulSoup
import requests


class Plugin:
    def __init__(self):
        pass

    def news(self):
        response = requests.get(
            "https://www.bbc.co.uk/news/world"
        )  # gets the world news
        doc = BeautifulSoup(response.text, "html.parser")  # parses website
        headlines = doc.find_all("h3")  # finds headlines
        # now headlines have a newline at the start and the end so
        # we want to get rid of thi hence the wierd indexes for headline.text
        # we also only want the first 10 headlines
        ten_headlines_text_list = [headline.text[:] for headline in headlines[:10]]
        return ten_headlines_text_list  # return the list as a string with newlines

    def run(self, incoming, methods, info, bot_info):
        try:
            if info["command"] == "PRIVMSG" and info["args"][1] == ".news":
                for headline in Plugin.news(self):
                    methods["send"](info["address"], headline)
        except Exception as e:
            print("woops news plugin error ", e)
