"""
script to generate plugins info
"""

import os
import importlib.util

directory = os.fsencode(__file__[:-13] + "/plugins")

def docFind(lines, att):
    hit = False

    for line in lines.splitlines():

        if hit:
            auth = str(line)
            auth = auth.strip()
            return auth

        if line == f"[{att}]":
            hit = True

    return f"Unknown {att}"


f = open(__file__[:-13] + "/plugins_info.md", "w")
plug = ""

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith(".py"):
        spec = importlib.util.spec_from_file_location(filename[:-3], __file__[:-13] + "plugins/" + filename)
        x = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(x)

        if isinstance(x.__doc__, str):
            plug += filename + "\\" + "\n"
            plug += "by " + docFind(x.__doc__, "Author") + ", " + docFind(x.__doc__, "Website") + "\\" + "\n"
            plug += docFind(x.__doc__, "About") + "\n" + "\n"

f.write(plug)
f.close()
