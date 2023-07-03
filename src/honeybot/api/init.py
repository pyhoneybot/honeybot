import os
import shutil
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent
MAIN_DIR = CURRENT_DIR.parent
PLUGINS_DIR = os.path.join(MAIN_DIR, "plugins")
SETTINGS_DIR = os.path.join(MAIN_DIR, "settings")
TOML_SETTINGS_FILE = os.path.join(MAIN_DIR, "settings", "settings.toml")


def init(info):
    try:
        shutil.copytree(PLUGINS_DIR, os.path.join(info["cwd"], "plugins"))
        try:
            os.mkdir(os.path.join(info["cwd"], "settings"))
        except:
            pass
        shutil.copy(TOML_SETTINGS_FILE, os.path.join(info["cwd"], "settings", "settings.toml"))
    except FileExistsError:
        pass
    print("created!")
