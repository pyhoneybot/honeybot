# -*- coding: utf-8 -*-
"""
[russian_roulette.py]
Russian Roulette Plugin

[Author]
Angelo Giacco

[About]
In the original russian roulette, you have a one sixth chance of committing
suicide. In this version, you have a one sixth chance of being kicked from
the channel. The bot will utilise the IRC command:
/kick #channel nickname
where #channel is the channel name and nicknames is the nickname of the user

[Commands]
>>> .russian_roulette
either returns a string saying you survived or kicks you off the channel
"""
import random

class Plugin:

    def __init__(self):
        pass

    def risk(self, incoming, methods, info):
        kill = True if random.random() < 0.2 else False #should the user be kicked
        if kill:
            name = info["prefix"].split("!")[0]
            channel = info["address"]
            kill_command = "/kick "+ channel + " " + name + " \r\n"
            methods["send_raw"](kill_command)
            #code to quit the channel
            return "Suicide is always a risk when playing russian roulette... RIP..."
        else:
            return "You survived..."

    def run(self, incoming, methods, info):
        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.russian_roulette':
                methods['send'](info['address'], Plugin.risk(self, incoming, methods, info))
        except Exception as e:
            print('woops russian roulette plugin error ', e)
