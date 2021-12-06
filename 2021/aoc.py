import importlib
import sys

day = sys.argv[1]
part = sys.argv[2]

with open(f'day{day}input.txt') as f:
    module = importlib.import_module(f'day{day}')
    text = f.read()[:-1]
    try:
        mapper = getattr(module, 'mapper')
        text = mapper(text)
    except AttributeError:
        pass
    print(getattr(module, f'part{part}')(text))
