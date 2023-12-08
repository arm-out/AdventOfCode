from utils import getInput

inputs = getInput(8)

dirs = inputs[0]
nodes = {}
for line in inputs[2:]:
    line = line.split()
    nodes[line[0]] = (line[2][1:-1], line[3][:-1])

curr = 'AAA'
steps = 0
dirs_idx = 0
while curr != 'ZZZ':
    if dirs[dirs_idx] == 'R':
        curr = nodes[curr][1]
    else:
        curr = nodes[curr][0]
    
    dirs_idx = (dirs_idx + 1) % len(dirs)
    steps += 1

print(steps)

