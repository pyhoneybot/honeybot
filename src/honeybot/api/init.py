import shutil
from pathlib import Path  # noqa E402
import os

CURRENT_DIR = Path(__file__).parent
MAIN_DIR = CURRENT_DIR.parent
PLUGINS_DIR = os.path.join(MAIN_DIR, 'plugins')
SETTINGS_DIR = os.path.join(MAIN_DIR, 'settings')


def init(info):
    try:
        shutil.copytree(PLUGINS_DIR, os.path.join(info['cwd'], 'plugins'))
        shutil.copytree(SETTINGS_DIR, os.path.join(info['cwd'], 'settings'))
    except FileExistsError:
        pass
    print('created!')
