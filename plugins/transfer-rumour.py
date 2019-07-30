# -*- coding: utf-8 -*-
"""
[transfer-rumour.py]
Transfer Rumour Plugin

[Author]
Angelo Giacco

[About]
Collects transfer rumours from BBC sport

[Commands]
>>> .transfer-rumour
prints the top transfer rumour
"""
import requests
from bs4 import BeautifulSoup

class Plugin:
    def __init__(self):
        pass

    def collect_rumour(methods,info):
        r = requests.get("https://www.bbc.co.uk/sport/football/gossip")
        soup = BeautifulSoup(r.content,features="html5lib")
        content = soup.find("div",attrs={"class":"story-body"})

        for rumour in content.findAll('p'):
            for anchor in rumour.findAll('a'):
                anchor.decompose()
            try:
                if len(rumour.text)>0:
                    methods["send"](info["address"],rumour.text)
            except TypeError:
                continue

    def run(self, incoming, methods, info, bot_info):

        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.transfer-rumour':
                methods['send'](info['address'], Plugin.collect_rumour(methods,info))
        except Exception as e:
            print('woops plug', e)
