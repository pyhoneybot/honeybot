
def set_nick(name):
    return 'NICK {0} \r\n'.format(name)

def present(name):
    return 'USER {0} {0} {0} : {0} IRC\r\n'.format(name)

def identify(password):
    return 'msg NickServ identify {0} \r\n'.format(password)

def join_channel(channel):
    return 'JOIN {0} \r\n'.format(channel)

def specific_send(target, msg):
    return "PRIVMSG {0} :{1}\r\n".format(target, msg)

def pong_return(domain):
    return 'PONG :{}\r\n'.format(domain)