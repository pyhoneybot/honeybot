import os
from importlib import import_module

directory = os.fsencode("./")


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


f = open("./plugins_info.md", "w")
plug = ""

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith(".py"):
        x = import_module(filename[:-3])

        if isinstance(x.__doc__, str):
            plug += filename + "\\" + "\n"
            plug += "by " + docFind(x.__doc__, "Author") + ", " + docFind(x.__doc__, "Website") + "\\" + "\n"
            plug += docFind(x.__doc__, "About") + "\n" + "\n"

f.write(plug)
f.close()
