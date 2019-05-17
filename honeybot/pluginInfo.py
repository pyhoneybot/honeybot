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
        try:
            spec = importlib.util.spec_from_file_location(filename[:-3], __file__[:-13] + "plugins/" + filename)
            x = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(x)
        except:
            print('skipped')

        if isinstance(x.__doc__, str):
            plug += "# " + filename + "\n"
            plug += "by " + docFind(x.__doc__, "Author")
            if docFind(x.__doc__, "Website") != "Unknown Website":
                plug += ", " + "[Website](" + docFind(x.__doc__, "Website") + ")\\\n"
            else:
                plug += "\\\n"

            plug += docFind(x.__doc__, "About") + "\n"
            if docFind(x.__doc__, "Commands") != "Unknown Commands":
                plug += "\\\n<code>" + docFind(x.__doc__, "Commands").replace(">>> ","").replace("<","\\<") + "</code>" + "\n"
            else:
                plug += "\\\n"
            plug += "\n"

f.write(plug)
f.close()
