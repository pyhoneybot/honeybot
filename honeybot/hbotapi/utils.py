def prevent_none(x):
    return x if x else ''


def configfile_to_list(filename):
    elements = []
    with open('settings/{}.conf'.format(filename)) as f:
        elements = f.read().split('\n')
        elements = list(filter(lambda x: x != '', elements))
    return elements


def get_requirements():
    reqs = []
    with open('../requirements.txt') as f:
        reqs = f.read().split('\n')
    reqs = [m.split('==')[0] for m in reqs if m]
    return reqs