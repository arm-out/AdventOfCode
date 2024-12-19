from utils import getInput
from functools import cache

inputs = getInput(19)
towels = inputs[0].split(', ')
patterns = inputs[2:]

@cache
def search(pat):
    if pat == '':
        return 1
    
    n = 0
    for towel in towels:
        if pat.startswith(towel):
            n += search(pat[len(towel):])
    
    return n

res = 0
for p in patterns:
    res += search(p)

print(res)