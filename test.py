import unittest
import configparser
from main import Bot_core as Bot
'''
':appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/ip.200.200.22.200 PRIVMSG ##bottestingmu :ef'
{
'prefix': 'appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/ip.200.200.22.200',
'command': 'PRIVMSG',
'address': '##bottestingmu',
'args': ['##bottestingmu', 'ef']
}
'''
config = configparser.ConfigParser()
config.read('CONNECT.conf')

# incoming
incoming = ':appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/ip.200.200.22.200 PRIVMSG ##bottestingmu :ef'
bot = Bot()


class HoneybotTests(unittest.TestCase):
    '''
    basic info
    '''
    def test_name(self):
        self.assertEqual(
            bot.name,
            config['INFO']['name'])

    def test_server_url(self):
        self.assertEqual(
            bot.server_url,
            config['INFO']['server_url'])

    def test_port(self):
        self.assertEqual(
            bot.port,
            int(config['INFO']['port']))
    '''
    info function
    '''
    def test_info_prefix(self):
        self.assertEqual(
            bot.info(incoming)['prefix'],
            'appinv!c5e342c5@gateway/web/cgi-irc/kiwiirc.com/ip.200.200.22.200')

    def test_info_command(self):
        self.assertEqual(
            bot.info(incoming)['command'],
            'PRIVMSG')

    def test_info_address(self):
        self.assertEqual(
            bot.info(incoming)['address'],
            '##bottestingmu')

    def test_info_args(self):
        self.assertEqual(
            bot.info(incoming)['args'],
            ['##bottestingmu', 'ef'])

    '''
    commands
    '''
    def test_set_nick_command(self):
        self.assertEqual(
            bot.set_nick_command(),
            'NICK {0}\r\n'.format(config['INFO']['name'])
        )

    def test_present_command(self):
        self.assertEqual(
            bot.present_command(),
            'USER {0} {0} {0} : {0} IRC\r\n'.format(config['INFO']['name'])
        )

    def test_identify_command(self):
        self.assertEqual(
            bot.identify_command(),
            'msg NickServ identify  \r\n'
        )

    def test_join_command(self):
        self.assertEqual(
            bot.join_channel_command('#abc'),
            'JOIN #abc \r\n'
        )

    def test_specific_send_command(self):
        self.assertEqual(
            bot.specific_send_command('#abc', 'greetings'),
            'PRIVMSG #abc :greetings\r\n'
        )

    def test_pong_return(self):
        self.assertEqual(
            bot.pong_return(),
            'PONG \r\n'
        )



if __name__ == '__main__':
    unittest.main()
