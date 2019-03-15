# -*- coding: utf-8 -*-
"""
[weather.py]
Weather Plugin
[Author]
Gabriele Ron
[About]
A plugin to get the weather of a location
[Commands]
>>> .weather <city> <country code>
returns the weather
"""

import requests

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.weather':
                api_url = f"api.openweathermap.org/data/2.5/weather?q={info['args'][2]},{info['args'][3]}" \
                    f"&APPID=8801bc666d30a8cc9294feaf60c01117"
                response = requests.get(api_url)
                response_json = response.json()

                weather = f"The weather for {response_json['name']} is {response_json['weather'][0]['description']} at " \
                    f"{response_json['main']['temp']} degrees"

                methods['send'](info['address'], weather)
        except Exception as e:
            print('woops plugin error ', e)
