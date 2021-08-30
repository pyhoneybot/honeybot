#!/usr/bin/env python3
#!/usr/bin/env python2
import logging
import sys
import argparse
import os

from honeybot.api.main import Bot_core
from honeybot.api.print import print_connect_settings
from honeybot.api.print import print_honeybot_manifesto
from honeybot.api.generate import gen_pluginsinfo
from honeybot.api.init import init 

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("botsetting", choices=["run", "gen_pluginsinfo", "init"])

    args = parser.parse_args()

    info = {
        'cwd': os.getcwd(),
        'settings_path': os.path.join(os.getcwd(), 'settings'),
    }

    print_honeybot_manifesto(info)
    if args.botsetting == "run":
        
        print_connect_settings(info)
        try:
            x = Bot_core(info)
            x.unregistered_run()
        except KeyboardInterrupt:
            print("interrupted")
            sys.exit()

    elif args.botsetting == "gen_pluginsinfo":
        gen_pluginsinfo()

    elif args.botsetting == "init":
        init(info)

if __name__ == '__main__':
    main()
