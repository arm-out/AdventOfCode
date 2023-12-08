from utils import getInput
from math import gcd
from functools import reduce

inputs = getInput(8)

dirs = inputs[0]
nodes = {}
for line in inputs[2:]:
    line = line.split()
    nodes[line[0]] = (line[2][1:-1], line[3][:-1])

positions = [x for x in nodes.keys() if x[-1] == 'A']
cycles = []

for curr in positions:
    cycle = []

    curr_dir = dirs
    steps = 0
    first_z = None

    while True:
        while steps == 0 or curr[-1] != 'Z':
            steps += 1
            curr = nodes[curr][0 if curr_dir[0] == 'L' else 1]
            curr_dir = curr_dir[1:] + curr_dir[0]
        
        cycle.append(steps)

        if first_z is None:
            first_z = curr
            steps = 0
        elif curr == first_z:
            break
    
    cycles.append(cycle)

print(reduce(lambda x, y: x*y//gcd(x, y), [x[0] for x in cycles]))