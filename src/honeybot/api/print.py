import configparser
import os

ascii_message = """
            _  _                   _         _
  _ __ _  _| || |___ _ _  ___ _  _| |__  ___| |_
 | '_ \ || | __ / _ \ ' \/ -_) || | '_ \/ _ \  _|
 | .__/\_, |_||_\___/_||_\___|\_, |_.__/\___/\__|
 |_|   |__/                   |__/
 github.com/pyhoneybot/honeybot
 ~ IRC bot with awesome plugins
"""


def print_honeybot_manifesto(info):
    print(ascii_message)


def print_connect_settings(info):
    settings_path = os.path.join(info['settings_path'], "CONNECT.conf")
    connect_config = configparser.ConfigParser()
    connect_config.read(settings_path)
    server_url = connect_config["INFO"]["server_url"]
    port = connect_config["INFO"]["port"]
    name = connect_config["INFO"]["name"]

    print("connecting with settings:")
    print("server url:", server_url)
    print("port:", port)
    print("username:", name)
    print('-'*3)
