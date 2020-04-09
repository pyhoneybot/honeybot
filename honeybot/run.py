#!/usr/bin/env python3
#!/usr/bin/env python2
import logging
import sys

from main import Bot_core
from hbotapi.utils import print_connect_settings
from hbotapi.utils import print_honeybot_manifesto

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warn message")
# logger.error("error message")
# logger.critical("critical message")
print_honeybot_manifesto()
print_connect_settings()
try:
    x = Bot_core()
    x.unregistered_run()
except KeyboardInterrupt:
    print('interrupted')
    sys.exit()
