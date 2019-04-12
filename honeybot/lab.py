import importlib

reqs = []
with open('../requirements.txt') as f:
    reqs = f.read().split('\n')


reqs = [m.split('==')[0] for m in reqs if m]

for module in reqs:
    try:
        importlib.import_module(module)
    except ModuleNotFoundError as e:
        print('not found:', module)
print(reqs)
