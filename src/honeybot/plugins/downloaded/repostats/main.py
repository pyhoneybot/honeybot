# -*- coding: utf-8 -*-
"""
[repostats.py]
Repostats Plugin

[Author]
Shreyansh Sancheti

[About]
Gets the number of forks and stars for a given repo

[Commands]
>>> .repostats url
returns starcount stars | forkcount forks
"""


from urllib.parse import urlparse

import bs4 as bs
import requests


class Plugin:
    def __init__(self):
        pass

    def repostats(self, url):
        try:
            source = requests.get(url).text
            soup = bs.BeautifulSoup(source, "lxml")
            u = urlparse(url).path
            username = u.rpartition("/")[0]
            username = username.replace("/", "")
            reponame = u.rpartition("/")[2]
            hstar = "/" + username + "/" + reponame + "/stargazers"
            hfork = "/" + username + "/" + reponame + "/network/members"
            star = int(soup.find("a", href=hstar).get_text())
            fork = int(soup.find("a", href=hfork).get_text())
            return star + "stars |" + fork + "forks"
        except Exception:
            return "Repo doesn't exist"

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            print(len(msgs))
            if info["command"] == "PRIVMSG" and msgs[0] == ".repostats":
                url = int(msgs[1])
                methods["send"](info["address"], Plugin.repostats(self, url))
        except Exception as e:
            print("woops plugin error: ", e)
