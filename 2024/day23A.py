from utils import getInput
from collections import defaultdict

inputs = getInput(23)
connections = defaultdict(set)

for con in inputs:
    a, b = con.split("-")
    connections[a].add(b)
    connections[b].add(a)

sets = set()
for x in connections:
    for y in connections[x]:
        for z in connections[y]:
            if z != x and z in connections[x]:
                sets.add(tuple(sorted([x, y, z])))

res = 0
for s in sets:
    if any([x[:1] == "t" for x in s]):
        res += 1

print(res)