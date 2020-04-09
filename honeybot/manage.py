#!/usr/bin/env python3
#!/usr/bin/env python2
import logging
import sys
import argparse

from main import Bot_core
from hbotapi.print import print_connect_settings
from hbotapi.print import print_honeybot_manifesto
from hbotapi.generate import gen_pluginsinfo

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


parser = argparse.ArgumentParser()
   
parser.add_argument('botsetting', choices=['runbot', 'gen_pluginsinfo'])

args = parser.parse_args()

if args.botsetting == 'runbot':
    print_honeybot_manifesto()
    print_connect_settings()
    try:
        x = Bot_core()
        x.unregistered_run()
    except KeyboardInterrupt:
        print('interrupted')
        sys.exit()

elif args.botsetting == 'gen_pluginsinfo':
    gen_pluginsinfo()


