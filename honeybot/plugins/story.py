# -*- coding: utf-8 -*-
"""
[story.py]
Story Plugin

[Author]
Tuan Thai

[About]
Sends a random story

[Commands]
>>> .story
returns random story
"""

import random
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Plugin:
    def_init_(self):
        pass
        
        
    def story(self):
        stories = ["pea-blossom"]
        story_url = ("http://www.shortkidstories.com/story/" + str(random.choice(stories) + "/"))

        client = urlopen(story_url).read()

        soup = BeautifulSoup(client, "html.parser")
        texts = soup.find('div', class_= 'allStories')
        for paragraph in texts.findAll('p'):
            print(str(paragraph.text))
        
        
    def run(self, incoming, methods, info, bot_info):
        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.story':
                methods['send'](info['address'], Plugin.story(self))
        except Exception as e:
            print('woops plug: ', e)
