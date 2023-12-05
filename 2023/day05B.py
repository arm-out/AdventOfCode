import sys
from utils import getInput
import multiprocessing as mp

DAY = 5
getInput(DAY)

f = open("inputs/day05.txt", "r")
inputs, *blocks = f.read().split("\n\n")

inputs = list(map(int, inputs.split(':')[1].split()))
seeds = []
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    
    new = []
    while seeds:
        s, e = seeds.pop()
        for dst, src, r in ranges:
            os = max(s, src)
            oe = min(e, src + r)
            if os < oe:
                new.append((os - src + dst, oe - src + dst))
                if os > s:
                    seeds.append((s, os))
                if oe < e:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))
    seeds = new

print(min(seeds)[0])

