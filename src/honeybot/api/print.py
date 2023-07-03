import configparser
import os
import sys

ascii_message = r"""
            _  _                   _         _
  _ __ _  _| || |___ _ _  ___ _  _| |__  ___| |_
 | '_ \ || | __ / _ \ ' \/ -_) || | '_ \/ _ \  _|
 | .__/\_, |_||_\___/_||_\___|\_, |_.__/\___/\__|
 |_|   |__/                   |__/
 github.com/pyhoneybot/honeybot
 ~ IRC bot with awesome plugins
"""


def tab(s=3):
    return ' ' * s

def line(n=3):
    return '-'*3


def status(symbol_type):
    if symbol_type in '!i>x':
        return '[' + symbol_type + ']'
    else:
        raise Exception('Undefined symbol type')

def print_honeybot_manifesto(info):
    print(ascii_message)


def print_connect_settings(info):
    settings_path = os.path.join(info["settings_path"], "CONNECT.conf")
    if not os.path.exists(settings_path):
        print('Could not find CONNECT.conf in', info["settings_path"])
        print('Make sure you are in the right folder')
        sys.exit()
    connect_config = configparser.ConfigParser()
    connect_config.read(settings_path)
    server_url = connect_config["INFO"]["server_url"]
    port = connect_config["INFO"]["port"]
    name = connect_config["INFO"]["name"]

    print(status('i')+" connecting with settings:")
    print(tab()+" server url:", server_url)
    print(tab()+" port:", port)
    print(tab()+" username:", name)
    print(line())
