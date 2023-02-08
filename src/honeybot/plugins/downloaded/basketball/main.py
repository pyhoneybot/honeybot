# -*- coding: utf-8 -*-
"""
[basketball.py]
Basketball Plugin

[Author]
Konstantinos Efthymiadis

[About]
Given the event and year as parameters, the plugin will return the countries that won the medal that year
Given the event and country as parameters, the plugin will return the number of medals this country has won

[Commands]
>>> .basketball <<event>> <<year/country>>
returns a string with all the information
>>> .basketball <<event>> <<all>>
returns a table with all the medals of all the years
"""

dataEuroBasket = {
    "1935": ["Latvia", "Spain", "Czechoslovakia", "24-18"],
    "1937": ["Lithuania", "Italy", "France", "24-23"],
    "1939": ["Lithuania", "Latvia", "Poland", "No playOffs"],
    "1946": ["Czechoslovakia", "Italy", "Hungary", "34-32"],
    "1947": ["USSR", "Czechoslovakia", "Egypt", "56-37"],
    "1949": ["Egypt", "France", "Greece", "No playOffs"],
    "1951": ["USSR", "Czechoslovakia", "France", "45-44"],
    "1953": ["USSR", "Hungary", "France", "No playOffs"],
    "1955": ["Hungary", "Czechoslovakia", "USSR", "No playOffs"],
    "1957": ["USSR", "Bulgaria", "Czechoslovakia", "No playOffs"],
    "1959": ["USSR", "Czechoslovakia", "France", "No playOffs"],
    "1961": ["USSR", "Yugoslavia", "Bulgaria", "60-53"],
    "1963": ["USSR", "Poland", "Yugoslavia", "61-45"],
    "1965": ["USSR", "Yugoslavia", "Poland", "58-49"],
    "1967": ["USSR", "Czechoslovakia", "Poland", "89-77"],
    "1969": ["USSR", "Yugoslavia", "Czechoslovakia", "81-72"],
    "1971": ["USSR", "Yugoslavia", "Italy", "69-64"],
    "1973": ["Yugoslavia", "Spain", "USSR", "78-67"],
    "1975": ["Yugoslavia", "USSR", "Italy", "No playOffs"],
    "1977": ["Yugoslavia", "USSR", "Czechoslovakia", "74-61"],
    "1979": ["USSR", "Israel", "Yugoslavia", "98-76"],
    "1981": ["USSR", "Yugoslavia", "Czechoslovakia", "84-67"],
    "1983": ["Italy", "Spain", "USSR", "105-96"],
    "1985": ["USSR", "Czechoslovakia", "Italy", "120-89"],
    "1987": ["Greece", "USSR", "Yugoslavia", "103-101"],
    "1989": ["Yugoslavia", "Greece", "USSR", "98-77"],
    "1991": ["Yugoslavia", "Italy", "Spain", "88-73"],
    "1993": ["Germany", "Russia", "Croatia", "71-70"],
    "1995": ["Yugoslavia", "Lithuania", "Croatia", "96-90"],
    "1997": ["Yugoslavia", "Italy", "Russia", "61-49"],
    "1999": ["Italy", "Spain", "Yugoslavia", "64-56"],
    "2001": ["Yugoslavia", "Turkey", "Spain", "78-69"],
    "2003": ["Lithuania", "Spain", "Italy", "93-84"],
    "2005": ["Greece", "Germany", "France", "78-62"],
    "2007": ["Russia", "Spain", "Lithuania", "60-59"],
    "2009": ["Spain", "Serbia", "Greece", "85-63"],
    "2011": ["Spain", "France", "Russia", "98-85"],
    "2013": ["France", "Lithuania", "Spain", "80-66"],
    "2015": ["Spain", "Lithuania", "France", "80-63"],
    "2017": ["Slovenia", "Serbia", "Spain", "93-85"],
    "2022": ["Spain", "France", "Germany", "88-76"]
}
dataWorldCup = {
    "1950": ["Argentina", "USA", "Chile", "64-50"],
    "1954": ["USA", "Brazil", "Philippines", "62-41"],
    "1959": ["Brazil", "USA", "Chile", "81-67"],
    "1963": ["Brazil", "Yugoslavia", "USSR", "90-71"],
    "1967": ["USSR", "Yugoslavia", "Brazil", "71-59"],
    "1970": ["Yugoslavia", "Brazil", "USSR", "80-55"],
    "1974": ["USSR", "Yugoslavia", "USA", "79-82"],
    "1978": ["Yugoslavia", "USSR", "Brazil", "82-81"],
    "1982": ["USSR", "USA", "Yugoslavia", "95-94"],
    "1986": ["USA", "USSR", "Yugoslavia", "87-85"],
    "1990": ["Yugoslavia", "USSR", "USA", "92-75"],
    "1994": ["USA", "Russia", "Croatia", "137-91"],
    "1998": ["Yugoslavia", "Russia", "USA", "64-62"],
    "2002": ["Yugoslavia", "Argentina", "Germany", "84-77"],
    "2006": ["Spain", "Greece", "USA", "70-47"],
    "2010": ["USA", "Turkey", "Lithuania", "81-64"],
    "2014": ["USA", "Serbia", "France", "129-92"],
    "2019": ["Spain", "Argentina", "France", "95-75"]
}


class Plugin:
    def __init__(self):
        pass

    def __accordingToYear__(year, event):
        dataEvent = {}
        if event == "eu":
            dataEvent = dataEuroBasket
        elif event == "wc":
            dataEvent = dataWorldCup

        if year in dataEvent:
            data = dataEvent.get(year)
            text = "Gold: " + data[0] + "\nSilver: " + data[1] + "\nBronze: " + data[2]
            if data[3] != "No playOffs":
                text += "\nFinal Score:\n" + data[0] + " " + data[3] + " " + data[1]
            return text
        else:
            return "No results for that year"

    def __accordingToCountry__(country, event):
        dataEvent = {}
        if event == "eu":
            dataEvent = dataEuroBasket
        elif event == "wc":
            dataEvent = dataWorldCup

        goldMedal = 0
        silverMedal = 0
        bronzeMedal = 0

        for value in dataEvent.values():
            if value[0].upper() == country.upper():
                goldMedal += 1
            elif value[1].upper() == country.upper():
                silverMedal += 1
            elif value[2].upper() == country.upper():
                bronzeMedal += 1

        if goldMedal == silverMedal and silverMedal == bronzeMedal and bronzeMedal == 0:
            return "The country: " + country + " does not have any medal"
        else:
            text = country + " Medals:\n" + "Gold: " + str(goldMedal) + "\nSilver: " + str(
                silverMedal) + "\nBronze: " + str(bronzeMedal) + "\nTotal Medals: " + str(
                goldMedal + silverMedal + bronzeMedal)
            return text

    def __createTable__(maxLen, word):
        whiteCharacters = maxLen - len(word)
        text = ""
        for i in range(0, whiteCharacters // 2):
            text += " "
        text += word
        for i in range(whiteCharacters // 2, whiteCharacters):
            text += " "
        text += "|"
        return text

    def __allTheMedalsAllTheYears__(event):
        dataEvent = {}
        text=""
        if event == "eu":
            dataEvent = dataEuroBasket
            text="European Basketball Championship\n"
        elif event == "wc":
            dataEvent = dataWorldCup
            text="FIBA Basketball World Cup\n"

        if not dataEvent:
            return

        maxForGold = -1
        maxForSilver = -1
        maxForBronze = -1

        for value in dataEvent.values():
            if len(value[0]) > maxForGold:
                maxForGold = len(value[0])
            if len(value[1]) > maxForSilver:
                maxForSilver = len(value[1])
            if len(value[2]) > maxForBronze:
                maxForBronze = len(value[2])

        goldMedal = "Gold Medal"
        silverMedal = "Silver Medal"
        bronzeMedal = "Bronze Medal"

        if len(goldMedal) > maxForGold:
            maxForGold = len(goldMedal)
        if len(silverMedal) > maxForSilver:
            maxForSilver = len(silverMedal)
        if len(bronzeMedal) > maxForBronze:
            maxForBronze = len(bronzeMedal)

        text += "|Year|"
        text += Plugin.__createTable__(maxForGold, goldMedal)
        text += Plugin.__createTable__(maxForSilver, silverMedal)
        text += Plugin.__createTable__(maxForBronze, bronzeMedal)
        text += "\n"

        for key in dataEvent.keys():
            text += "|" + key + "|"
            temp = dataEvent.get(key)

            text += Plugin.__createTable__(maxForGold, temp[0])
            text += Plugin.__createTable__(maxForSilver, temp[1])
            text += Plugin.__createTable__(maxForBronze, temp[2])
            text += "\n"

        return text

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and len(msgs) == 3 and msgs[0] == ".basketball":
                event = msgs[1]
                if msgs[2] == "all":
                    methods["send"](info["address"], Plugin.__allTheMedalsAllTheYears__(msgs[1]))
                elif msgs[2].isnumeric():
                    methods["send"](info["address"], Plugin.__accordingToYear__(msgs[2], msgs[1]))
                else:
                    methods["send"](info["address"], Plugin.__accordingToCountry__(msgs[2], msgs[1]))

        except Exception as e:
            print("Something Wrong. There is a Plugin Error: ", e)
