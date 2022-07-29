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
from bs4 import BeautifulSoup
import requests
import datetime
import string


class Plugin:
    def __init__(self):
        pass

    def scrape(self, country):
        response = requests.get(
            "https://www.worldometers.info/coronavirus/"
        )  # gets the coronavirus statistcs
        doc = BeautifulSoup(response.text, "html.parser")  # parses website
        cases = doc.find_all(class_="maincounter-number")
        data = doc.find_all("td")
        if country == "global":
            most_affected = (
                []
            )  # each element is an array as follows [country,cases,deaths]
            for index in range(0, 45, 11):
                most_affected.append(
                    [
                        str(data[index].text),
                        str(data[index + 1].text),
                        str(data[index + 3].text.strip()),
                    ]
                )
            today = str(datetime.date.today())
            msg = (
                "The latest coronavirus pandemic figures as of "
                + today
                + " show "
                + " that there are currently "
                + str(cases[0].text.strip())
                + " cases of "
                + "coronavirus of which "
                + str(cases[2].text.strip())
                + " have recovered. "
                + "Unfortunately, "
                + str(cases[1].text.strip())
                + " patients have died as a "
                + "result of the coronavirus pandemic. May they rest in peace."
            )
            msg += "The most affected countries are the following: \n"
            for c in most_affected:
                country = c[0]
                total_cases = c[1]
                deaths = c[2]
                string = (
                    country
                    + " has "
                    + total_cases
                    + " confirmed cases that have led to "
                    + deaths
                    + " deaths. RIP \n"
                )
                msg += string
            return msg
        else:
            name_confusion = {
                "United Kingdom": "UK",
                "United States": "USA",
                "Uk": "UK",
                "America": "USA",
                "Usa": "USA",
                "United States Of America": "USA",
                "South Korea": "S. Korea",
                "Czech Republic": "Czechia",
                "Faroe Islands": "Faeroe Islands",
                "United Arab Emirates": "UAE",
                "Uae": "UAE",
                "Democratic Republic Of Congo": "DRC",
                "Drc": "DRC",
                "United States Virgin Islands": "U.S. Virgin Islands",
                "Central African Republic": "CAR",
                "Car": "CAR",
            }
            if country in name_confusion:
                country = name_confusion[country]
            for index in range(0, len(data) - 11, 11):
                name = data[index].text
                if data[index].text == country:
                    today = str(datetime.date.today())
                    cases = data[index + 1].text
                    deaths = data[index + 3].text
                    recovered = data[index + 5].text
                    msg = (
                        "The latest coronavirus pandemic figures as of "
                        + today
                        + " for "
                        + name
                        + " show"
                        + " that there are currently "
                        + cases
                        + " cases of coronavirus in "
                        + name
                        + "."
                    )
                    if recovered != " ":
                        msg += " Of these " + recovered + " have recovered. "
                    else:
                        msg += " None have recovered yet. "
                    if deaths != " ":
                        msg += (
                            "Unfortunately, "
                            + deaths.strip()
                            + " patients in "
                            + name
                            + " have died as a "
                            + "result of the coronavirus pandemic. May they rest in peace."
                        )
                    else:
                        msg += (
                            "Fortunately nobody has died yet in "
                            + name
                            + " as a result of coronavirus."
                        )
                    return msg
                    break
            else:
                msg = "Invalid country input"
                return msg

    def run(self, incoming, methods, info, bot_info):
        try:
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG" and msgs[0] == ".corona":
                if len(msgs) == 1:
                    headlines = Plugin.scrape(self, "global")
                    for line in headlines.splitlines():
                        methods["send"](info["address"], line)
                else:
                    country_name = " ".join(msgs[1:])
                    country_name = string.capwords(country_name)
                    msg = Plugin.scrape(self, country_name)
                    methods["send"](info["address"], msg)

        except Exception as e:
            print("woops, corona plugin error", e)
