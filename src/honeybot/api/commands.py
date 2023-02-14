def set_nick(name):
    return f"NICK {name} \r\n"


def present(name):
    return "USER {0} {0} {0} : {0} IRC\r\n".format(name)


def identify(password):
    return f"msg NickServ identify {password} \r\n"


def join_channel(channel):
    return f"JOIN {channel} \r\n"


def specific_send(target, msg):
    return f"PRIVMSG {target} :{msg}\r\n"


def pong_return(domain):
    return f"PONG :{domain}\r\n"
