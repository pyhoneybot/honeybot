# -*- coding: utf-8 -*-
"""
[password_generator.py]
Password Generator Plugin

[Author]
Nishant, JPMorgan Chase & Co.

[About]
sends different type of passwords

[Commands]
>>> .passgen <<length>>
returns alphabetic password of specified length

>>> .passgensecure <<length>>
returns secure alphanumeric password of specified length

>>> .passgenalphanum <<length>>
returns alphanumeric password of specified length

>>> .passgenspecialchar <<length>>
returns universally accepted alphanumeric password with
special characters of specified length where length >= 4
"""

import random
import secrets
import string


class Plugin:
    def __init__(self):
        pass

    def __passgen(password_length):
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for i in range(password_length))

    def __passgenalphanum(password_length):
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(
            random.choice(password_characters) for i in range(password_length)
        )

    def __passgensecure(password_length):
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(
            secrets.choice(password_characters) for i in range(password_length)
        )

    def __passgenspecialchar(password_length):
        randomSource = string.ascii_letters + string.digits + string.punctuation
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        for i in range(password_length - 4):
            password += random.choice(randomSource)
        passwordList = list(password)
        random.SystemRandom().shuffle(passwordList)
        password = "".join(passwordList)
        return password

    def __securePasswordGenerator():
        password = ""
        person = ["I", "i", "He", "he", "She", "she", "It", "it"]
        verb = [
            ["am", "is"],
            ["run", "runs"],
            ["go", "goes"],
            ["drink", "drinks"],
            ["eat", "eats"],
            ["sleep", "sleeps"],
            ["like", "likes"],
        ]
        prep = ["to", "under", "along", "within", "until", "into"]
        article = ["the", "a"]
        thing = ["bridge", "car", "store", "shirt", "computer", "bed", "couch"]

        password += person[random.randint(0, len(person) - 1)]

        if password == person[0] or password == person[1]:
            password += verb[random.randint(0, len(verb) - 1)][0]
        else:
            password += verb[random.randint(0, len(verb) - 1)][1]

        password += prep[random.randint(0, len(prep) - 1)]
        password += article[random.randint(0, len(article) - 1)]
        password += thing[random.randint(0, len(thing) - 1)]

        char_converter = {"i": "1", "e": "3", "a": "@", " ": "-", "o": "0"}
        i = random.randint(0, 2)
        new = list(password)

        if i % 2 == 0:
            for i in range(len(password)):
                if new[i] in char_converter:
                    new[i] = char_converter[new[i]]
            new = "".join(new)
            return new

        else:
            num = round(len(password) / 2)
            for i in range(num + 1):
                if new[i] in char_converter:
                    new[i] = char_converter[new[i]]
            new = "".join(new)
            return new

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
            # print(info)
            msgs = info["args"][1:][0].split()
            if info["command"] == "PRIVMSG":
                if len(msgs) > 1:
                    if msgs[0] == ".passgen":
                        length = msgs[1]
                        methods["send"](info["address"], Plugin.__passgen(int(length)))
                    if msgs[0] == ".passgensecure":
                        length = msgs[1]
                        methods["send"](
                            info["address"], Plugin.__passgensecure(int(length))
                        )
                    if msgs[0] == ".passgenalphanum":
                        length = msgs[1]
                        methods["send"](
                            info["address"], Plugin.__passgenalphanum(int(length))
                        )
                    if msgs[0] == ".passgenspecialchar":
                        length = msgs[1]
                        if int(length) >= 4:
                            methods["send"](
                                info["address"],
                                Plugin.__passgenspecialchar(int(length)),
                            )
                        else:
                            raise Exception(
                                "Length of password should be greater than 4."
                            )
        except Exception as e:
            print("woops plug", e)
