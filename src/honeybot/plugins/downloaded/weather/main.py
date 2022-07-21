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

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()

            if info["command"] == "PRIVMSG" and msgs[0] == ".weather":
                api_url = (
                    f"https://api.openweathermap.org/data/2.5/weather?"
                    f"q={msgs[1]},{msgs[2]}"
                    f"&APPID=8801bc666d30a8cc9294feaf60c01117&units=metric"
                )
                response = requests.get(api_url)
                response_json = response.json()

                weather = (
                    f"The weather for {response_json['name']} is "
                    f"{response_json['weather'][0]['description']} at "
                    f"{int(response_json['main']['temp'])} degrees celsius"
                )
                methods["send"](info["address"], weather)
        except Exception as e:
            print("woops plugin error ", e)
