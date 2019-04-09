class Plugin:
    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        try:
            print("COOL FREAKING BEANS---------------------------------------------------------------------------------------")
            if info['command'] == 'PRIVMSG' and info['args'][1] == '.coolbeans':
                methods['send'](info['address'], 'cool beans')
        except Exception as e:
            print('woops plugin error: ', e)