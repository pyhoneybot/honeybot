import os
import importlib
import json

BASE_DIR = "plugins/downloaded"
STORE_DIR = "../../honeybot-store"

plugins = {"plugins": []}
dirs = [d for d in os.listdir(BASE_DIR) if not d.startswith("__")]


def pinfo(folder, attrib):
    try:
        mod = importlib.import_module("plugins.downloaded.{}.info".format(folder))
        return getattr(mod, attrib)
    except Exception as e:
        if attrib == "ORIGINAL_AUTHORS":
            return []
        else:
            return ""

    for d in dirs:
        NAME = pinfo(d, "NAME")
        ABOUT = pinfo(d, "ABOUT")
        ORIGINAL_AUTHORS = pinfo(d, "ORIGINAL_AUTHORS")
        COMMANDS = pinfo(d, "COMMANDS")
        WEBSITE = pinfo(d, "WEBSITE")
        plugins["plugins"].append(
            {
                "NAME": NAME,
                "ABOUT": ABOUT,
                "ORIGINAL_AUTHORS": ORIGINAL_AUTHORS,
                "COMMANDS": COMMANDS,
                "WEBSITE": WEBSITE,
                "FOLDER_NAME": d,
            }
        )

    print(plugins)

    with open(os.path.join(STORE_DIR, "plugins.json"), "w+") as f:
        json.dump(plugins, f, indent=4)
