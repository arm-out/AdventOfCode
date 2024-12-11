from utils import getInput
from functools import cache

inputs = getInput(11)
stones = list(map(int, inputs[0].split()))

@cache
def process(s, i):
    if i == 0:
        return 1
    
    if s == 0:
        return process(1, i - 1)
    string = str(s)
    length = len(string)
    if length % 2 == 0:
        left = int(string[:length // 2])
        right = int(string[length // 2:])
        return (process(left, i - 1) + process(right, i - 1))
    else:
        return process(str(int(s) * 2024), i - 1)
    
print(sum(process(stone, 75) for stone in stones))
