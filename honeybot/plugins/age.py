# -*- coding: utf-8 -*-
"""
[age.py]
Age Plugin

[Author]
Justin Walker

[About]
Given birthday it returns your age.

[Commands]
>>> .age <<day>> <<month>> <<year>>
returns age in yr/mo/day format.
"""

from datetime import date

class Plugin:
    def __init__(self):
        pass

    def __age(day, mo, yr):
        years = date.today().year - yr
        months = date.today().month - mo
        days = date.today().day - day
        if months < 0 or (months == 0 and day < 0):
            years -= 1

        msg = "You are {0}yrs. {1}mo. and {2} days old." \
              .format(years, abs(months), abs(days))
        return msg

    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()
            print(len(msgs))
            if info['command'] == 'PRIVMSG' and msgs[0] == '.age':
                if len(msgs) == 4 and len(msgs[1]) < 3 and \
                   len(msgs[2]) < 3 and len(msgs[3]) == 4:
                    day = int(msgs[1])
                    mo = int(msgs[2])
                    yr = int(msgs[3])
                    methods['send'](info['address'], Plugin.__age(day,mo,yr))
                else:
                    methods['send'](info['address'],
                            "Incorrect format. Should be '.age dy mo year -- -- ----'")
        except Exception as e:
            print('woops plugin error: ', e)