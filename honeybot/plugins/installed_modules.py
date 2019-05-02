# -*- coding: utf-8 -*-
"""
[installed_module.py]
Installation checker

[Author]
Abdur-Rahmaan Janhangeer, pythonmembers.club

[About]
checks if all listed in requirements.txt installed

[Commands]
>>> .installed
"""

import importlib

class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info, bot_info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.installed':
                reqs = bot_info['required_modules']
                not_found = []
                for module in reqs:
                    try:
                        importlib.import_module(module)
                    except ModuleNotFoundError as e:
                        print('not found:', module)
                        not_found.append(module)
                if not_found:
                    methods['send'](info['address'], 'not found:{}'.format('-'.join(not_found)))
                else:
                    methods['send'](info['address'], 'all required modules installed')
        except Exception as e:
            print('woops plug', e)
