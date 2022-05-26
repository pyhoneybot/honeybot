import unittest
import configparser
import traceback
from honeybot.api.main import Bot_core as Bot
import os
import time

"""
':appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/ip.200.200.22.200
PRIVMSG ##bottestingmu :ef'
{
'prefix': 'appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/ip.200.200.22.200',
'command': 'PRIVMSG',
'address': '##bottestingmu',
'args': ['##bottestingmu', 'ef']
}
"""

# Setup info
os.chdir("src/honeybot/")
root = os.getcwd()
settings = os.path.join(root, "settings")
config = configparser.ConfigParser()
config.read("settings/CONNECT.conf")
info = {'settings_path': settings, 'cwd': root}
# incoming
incoming = ":appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/ip.200.200.22.200 \
        PRIVMSG ##bottestingmu :ef"
bot = Bot(info)
sec = 5


class HoneybotTests(unittest.TestCase):
    """
    basic info
    """

    def test_name(self):
        self.assertEqual(bot.name, config["INFO"]["name"])

    def test_server_url(self):
        self.assertEqual(bot.server_url, config["INFO"]["server_url"])

    def test_port(self):
        self.assertEqual(bot.port, int(config["INFO"]["port"]))

    """
    info function
    """

    def test_info_prefix(self):
        self.assertEqual(
            bot.message_info(incoming)["prefix"],
            "appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/\
                    ip.200.200.22.200",
        )

    def test_info_command(self):
        self.assertEqual(bot.message_info(incoming)["command"], "PRIVMSG")

    def test_info_address(self):
        self.assertEqual(
            bot.message_info(incoming)["address"],
            "##bottestingmu")

    def test_info_args(self):
        self.assertEqual(
            bot.message_info(incoming)["args"],
            ["##bottestingmu", "ef"])


"""
commands
"""


def test_connect_command():
    unraised = True
    try:
        bot.connect()
        time.sleep(sec)
    except Exception as e:
        unraised = False
        print(repr(e))
        traceback.print_exc()
        assert unraised, "Connection Error!!!"
    finally:
        print("Testing IRC Connection...")


def test_join_command():
    unraised = True
    try:
        bot.join("#abc")
        time.sleep(sec)
    except Exception as e:
        unraised = False
        print(repr(e))
        traceback.print_exc()
        assert unraised, "Join Channel Error!!!"
    finally:
        print("Testing Joining Channel...")


def test_set_nick_command():
    unraised = True
    try:
        bot.greet()
        time.sleep(sec)
    except Exception as e:
        unraised = False
        print(repr(e))
        traceback.print_exc()
        assert unraised, "Nickname Setup Error!!!"
    finally:
        print("Testing Nickname Setup...")


def test_identify_command():
    unraised = True
    try:
        bot.identify()
        time.sleep(sec)
    except Exception as e:
        unraised = False
        print(repr(e))
        traceback.print_exc()
        assert unraised, "Identify Error!!!"
    finally:
        print("Testing Identifying Nickname...")


def test_specific_send_command():
    unraised = True
    try:
        bot.send_target("#abc", "greetings")
        time.sleep(sec)
    except Exception as e:
        unraised = False
        print(repr(e))
        traceback.print_exc()
        assert unraised, "Greetings Error!!!"
    finally:
        print("Testing Greetz...")


def test_pong_return():
    unraised = True
    try:
        bot.stay_alive("abc")
        time.sleep(sec)
    except Exception as e:
        unraised = False
        print(repr(e))
        traceback.print_exc()
        assert unraised, "Ping Error!!!"
    finally:
        print("Testing Ping... Pong...")


"""
Main Command Test
"""


def commands():
    test_connect_command()
    test_set_nick_command()
    test_join_command()
    test_identify_command()
    test_specific_send_command()
    test_pong_return()


if __name__ == "__main__":
    commands()
    unittest.main()
