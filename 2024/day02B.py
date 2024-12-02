from utils import getInput
from itertools import pairwise

inputs = getInput(2)

def check(levels):
    diffs = [b - a for a, b in pairwise(levels)]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)
    

safe = 0
for line in inputs:
    levels = [int(l) for l in line.split()]
    if check(levels):
        safe += 1
        continue
    
    if any(check(levels[:i] + levels[i+1:]) for i in range(len(levels))):
        safe += 1

print(safe)