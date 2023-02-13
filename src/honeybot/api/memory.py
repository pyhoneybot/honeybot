import configparser

memory_reader = configparser.ConfigParser()


def add_value(memfile, section, key, value):
    memory_reader.read(f"memory/{memfile}.txt")
    memory_reader[section][key] = value
    with open(f"memory/{memfile}.txt", "w") as file:
        memory_reader.write(file)


def remove_value(memfile, section, key):
    memory_reader.read(f"memory/{memfile}.txt")
    memory_reader.remove_option(section, key)
    with open(f"memory/{memfile}.txt", "w") as file:
        memory_reader.write(file)


def fetch_value(memfile, section, key):
    memory_reader.read(f"memory/{memfile}.txt")
    return memory_reader[section][key]
