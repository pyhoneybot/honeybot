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
returns universally accepted alphanumeric password with special characters of specified length where length >= 4
"""

import string, random, secrets


class Plugin:
    def __init__(self):
        pass

    def __passgen(self, password_length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(password_length))

    def __passgenalphanum(self, password_length):
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_characters) for i in range(password_length))

    def __passgensecure(self, password_length):
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(password_characters) for i in range(password_length))

    def __passgenspecialchar(self, password_length):
        randomSource = string.ascii_letters + string.digits + string.punctuation
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        for i in range(password_length - 4):
            password += random.choice(randomSource)
        passwordList = list(password)
        random.SystemRandom().shuffle(passwordList)
        password = ''.join(passwordList)
        return password

    def run(self, incoming, methods, info):
        try:
            # if '!~' in info['prefix']:
            # print(info)
            msgs = info['args'][1:][0].split()
            if info['command'] == 'PRIVMSG':
                if len(msgs) > 1:
                    if msgs[0] == '.passgen':
                        length = msgs[1]
                        methods['send'](info['address'], self.__passgen(length))
                    if msgs[0] == '.passgensecure':
                        length = msgs[1]
                        methods['send'](info['address'], self.__passgensecure(length))
                    if msgs[0] == '.passgenalphanum':
                        length = msgs[1]
                        methods['send'](info['address'], self.__passgenalphanum(length))
                    if msgs[0] == '.passgenspecialchar':
                        length = msgs[1]
                        if length >= 4:
                            methods['send'](info['address'], self.__passgenspecialchar(length))
                        else:
                            raise Exception('Length of password should be greater than 4.')
        except Exception as e:
            print('woops plug', e)
