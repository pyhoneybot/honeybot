# -*- coding: utf-8 -*-
"""
[horoscope.py]
Horoscope Plugin

[Author]
Angelo Giacco

[About]
Returns your daily horoscope based on your star sign
you can also enter your month and date of birth to automatically find your starsign
enter month and date as number

[Commands]
>>> .horoscope <<starsign>>
returns horoscope for starsign

.horoscope <<month>> <<day>>
returns horoscope for starsign of day entered
"""
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Required modules not found")

class Plugin:
    def __init__(self):
        pass

    def is_date_valid(month, day):
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])

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
            message = "That is not a valid star sign, check for typos"
        else:
            basic_url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="
            url = basic_url + signs[starsign]#creates the url
            content = requests.get(url) #gets the horoscope website
            doc = BeautifulSoup(content.text, 'html.parser') #parses website
            message = doc.find_all('p')[0].text #the first p element of the website is the horoscope and we only want its text
        return(message)

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()

            if info['command'] == 'PRIVMSG' and msgs[0] == '.horoscope':
                # The next message should be the star sign
                if len(msgs) > 3: # the message should only contain .horoscope and the user's star sign
                    methods['send'](info['address'], "too many messages")
                elif len(msgs) == 3:
                    month = msgs[1]
                    day = int(msgs[2])
                    def is_date_valid(month, day):
                        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                        return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])

                    #message = "month: "+month+" and day:"+day
                    #methods['send'](info['address'], message)

                    if month.lower() == 'december' or month == "12":
                        if is_date_valid(12,day):
                            astro_sign = 'sagittarius' if (day < 22) else 'capricorn'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'january' or month == "1":
                        if is_date_valid(1,day):
                            astro_sign = 'capricorn' if (day < 20) else 'aquarius'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'february' or month == "2":
                        if is_date_valid(2,day):
                            astro_sign = 'aquarius' if (day < 19) else 'pisces'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'march' or month == "3":
                        if is_date_valid(3,day):
                            astro_sign = 'pisces' if (day < 21) else 'aries'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'april' or month == "4":
                        if is_date_valid(4,day):
                            astro_sign = 'aries' if (day < 20) else 'taurus'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'may' or month == "5":
                        if is_date_valid(5,day):
                            astro_sign = 'taurus' if (day < 21) else 'gemini'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'june' or month == "6":
                        if is_date_valid(6,day):
                            astro_sign = 'gemini' if (day < 21) else 'cancer'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'july' or month == "7":
                        if is_date_valid(7,day):
                            astro_sign = 'cancer' if (day < 23) else 'leo'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'august' or month == "8":
                        if is_date_valid(8,day):
                            astro_sign = 'leo' if (day < 23) else 'virgo'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'september' or month == "9":
                        if is_date_valid(9,day):
                            astro_sign = 'virgo' if (day < 23) else 'libra'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'october' or month == "10":
                        if is_date_valid(10,day):
                            astro_sign = 'libra' if (day < 23) else 'scorpio'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    elif month.lower() == 'november' or month == "11":
                        if is_date_valid(11,day):
                            astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
                            methods['send'](info['address'], Plugin.horoscope(astro_sign))
                        else:
                            methods['send'](info['address'], "invalid day")
                    else:
                        methods['send'](info['address'], ".horoscope requires a valid month")
                elif len(msgs) == 2:
                    starsign = msgs[1]
                    methods['send'](info['address'], Plugin.horoscope(starsign))
                else:
                    methods['send'](info['address'], ".horoscope requires a star sign or day and month")

        except Exception as e:
            print('woops horoscope plugin error: ', e)
