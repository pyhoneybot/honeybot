# -*- coding: utf-8 -*-
"""
[corona.py]
Coronavirus Plugin

[Author]
Angelo Giacco

[About]
provides information about the coronavirus pandemic

[Commands]
>>> .corona
returns global coronavirus information

.corona <<country>>
returns coronavirus information for a specific country
"""

class Plugin:
    def __init__(self):
        pass

    def __scrape__(self,criteria="global"):
        if criteria == "global":
            response = requests.get('https://www.worldometers.info/coronavirus/') #gets the coronavirus statistcs
            doc = BeautifulSoup(response.text, 'html.parser') #parses website
            cases = doc.find_all(class_="maincounter-number")
            data = doc.find_all("td")
            most_affected = [] #each element is an array as follows [country,cases,deaths]
            for index in range(0,37,9):
                most_affected.append([str(data[index].text),str(data[index+1].text),str(data[index+3].text.strip())])
            today = str(datetime.date(datetime.now()))
            msg = "The latest coronavirus pandemic figures as of "+today+" show "+\
            " that there are currently "+str(cases[0].text.strip())+" cases of "+\
            "coronavirus of which "+ str(cases[2].text.strip()) +" have recovered. " +\
            "Unfortunately, "+ str(cases[1].text.strip()) + "patients have died as a "+\
            "result of the coronavirus pandemic. May they rest in peace. \n"
            msg += "The most affected countries are the following: \n"
            for c in most_affected:
                country = c[0]
                total_cases = c[1]
                deaths = c[2]
                msg += country +" has " + total_cases + " confirmed cases that have led to " + deaths +" deaths. RIP \n"
            return msg.rstrip()
        else:
            return "Coronavirus data for "+criteria

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info['args'][1].split()
            if info['command'] == 'PRIVMSG' and msgs[0] == '.corona':
                if len(msgs) > 2:
                    methods['send'](info['address'], 'Input not good. '+\
                    "Either enter .corona or .corona with a country name"+\
                    " afterwards! For example .corona UK")
                elif len(msgs) == 2:
                    methods['send'](info['address'], Plugin.scrape(msgs[1])))
                else:
                    methods['send'](info['address'], Plugin.scrape())

        except Exception as e:
            print('woops, corona plugin error', e)
