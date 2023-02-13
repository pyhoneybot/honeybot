class Commands:
    def set_nick(name):
        return f"NICK {name} \r\n"


print(Commands.set_nick("abc"))
