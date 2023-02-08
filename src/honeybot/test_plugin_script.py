# -*- coding: utf-8 -*-
""" Change to your plugin file name below.
                    ↓↓↓↓  """
import time

from plugins import basketball as test_plugin

test_plugin = test_plugin.Plugin


class Tester:
    def __init__(self, test_type, command):

        # Same methods as HoneyBot, but these print to screen
        methods = {"send_raw": self.send, "send": self.send_target, "join": self.join}

        # Set MOCK info for testing
        info = {
            "address": "##TestChannel",
            "args": ["##TestChannel"],
            "bot_name": "honeybot",
            "bot_special_command": "hbot",
            "command": "QUIT",
            "prefix": "TestAccount!~TestIdentity@192.168.123.123",
        }
        bot_info = {"time": time.time() - 12561}
        # time.sleep(5)

        # Update info with MOCK data.
        if test_type == "message":
            incoming = f":TestAccount!~TestIdentity@192.168.123.123 \
                PRIVMSG ##TestChannel :{command}"
            info["command"] = "PRIVMSG"
            info["args"] = [0, command]

        if test_type == "user_join":
            incoming = ":TestAccount!~TestIdentity@192.168.123.123 \
                JOIN ##TestChannel"
            info["command"] = "JOIN"

        if test_type == "user_quit":
            incoming = ":TestAccount!~TestIdentity@192.168.123.123 QUIT :"
            info["command"] = "QUIT"

        # Run plugin with above details
        test_plugin.run(self, incoming, methods, info, bot_info)

    def send(self, msg):
        print(msg)

    def join(self, channel):
        print(f"JOINING CHANNEL: {channel}")

    def send_target(self, target, msg):
        print(f"TO CHANNEL: {target}")
        print(f"MESSAGE: {msg}")


if __name__ == "__main__":
    """
    HOW TO USE:
        1. Add Plugin to plugins folder.
        2. Change plugin name at the top of this file.
        3. message
            3.1 Uses command as if a user was testing sending a message.
        4. join
            4.1 User joining a channel
        4. quit
            4.1 User quitting a channel
    """

    incoming_command_test = ".basketball eu all"

    Tester("message", incoming_command_test)
    # Tester('user_join', incoming_command_test)
    # Tester('user_quit', incoming_command_test)
