# -*- coding: utf-8 -*-
"""
[horoscope.py]
Horoscope Plugin

[Author]
Angelo Giacco

[About]
Returns your daily horoscope based on your star sign

[Commands]
>>> .horoscope <<star sign>>
prints star sign
"""
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Required modules not found")

class Plugin:
    def __init__(self):
        pass

    def horoscope(starsign):
        signs = dict()
        signs['aries'] = '1'
        signs['taurus'] = '2'
        signs['gemini'] = '3'
        signs['cancer'] = '4'
        signs['leo'] = '5'
        signs['virgo'] = '6'
        signs['libra'] = '7'
        signs['scorpio'] = '8'
        signs['sagittarius'] = '9'
        signs['capricorn'] = '10'
        signs['aquarius'] = '11'
        signs['pisces'] = '12'

        if starsign not in signs:
<<<<<<< HEAD
            message = "That is not a valid star sign, check for typos"
=======
            print("That is not a valid star sign, check for typos")
>>>>>>> 4d712bf982500de0814173276c74ea28a1e4be4f
        else:
            basic_url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="
            url = basic_url + signs[starsign]#creates the url
            content = requests.get(url) #gets the horoscope website
            doc = BeautifulSoup(content.text, 'html.parser') #parses website
            message = doc.find_all('p')[0].text #the first p element of the website is the horoscope and we only want its text
<<<<<<< HEAD
        return(message)
=======
            print(message)
>>>>>>> 4d712bf982500de0814173276c74ea28a1e4be4f

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()

            if info['command'] == 'PRIVMSG' and msgs[0] == '.horoscope':
                # The next message should be the star sign
<<<<<<< HEAD
                if len(msgs) > 2: # the message should only contain .horoscope and the user's star sign
                    methods['send'](info['address'], "too many messages")
                elif len(msgs) == 2:
                    starsign = msgs[1]
                    methods['send'](info['address'], Plugin.horoscope(starsign))
                else:
                    methods['send'](info['address'], ".horoscope requires a star sign")
=======
                term = ''
                if len(msgs) > 2: # the message should only contain .horoscope and the user's star sign
                    print("Too many messages")
                    raise Excepion
                elif (msgs) == 2:
                    starsign = msgs[1]
                    horoscope(starsign)
                else:
                    print(".horoscope requires a star sign")
>>>>>>> 4d712bf982500de0814173276c74ea28a1e4be4f

        except Exception as e:
            print('woops horoscope plugin error: ', e)
