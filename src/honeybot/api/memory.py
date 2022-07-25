import configparser

memory_reader = configparser.ConfigParser()


def add_value(memfile, section, key, value):
    memory_reader.read("memory/{}.txt".format(memfile))
    memory_reader[section][key] = value
    with open("memory/{}.txt".format(memfile), "w") as file:
        memory_reader.write(file)


def remove_value(memfile, section, key):
    memory_reader.read("memory/{}.txt".format(memfile))
    memory_reader.remove_option(section, key)
    with open("memory/{}.txt".format(memfile), "w") as file:
        memory_reader.write(file)


def fetch_value(memfile, section, key):
    memory_reader.read("memory/{}.txt".format(memfile))
    return memory_reader[section][key]
