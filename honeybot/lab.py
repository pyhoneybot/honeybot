import configparser

memory_reader = configparser.ConfigParser()
memory_reader.read('memory/global.txt')

memory_reader['VALUES']['b'] = '2'
memory_reader['VALUES']['c'] = '3'
memory_reader.remove_option('VALUES', 'b')

print(memory_reader['VALUES']['z'])

with open('memory/global.txt', 'w') as configfile:
    memory_reader.write(configfile)