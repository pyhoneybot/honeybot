class Commands:
    def set_nick(name):
        return "NICK {0} \r\n".format(name)


print(Commands.set_nick("abc"))
