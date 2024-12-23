from utils import getInput
from collections import defaultdict

inputs = getInput(23)
connections = defaultdict(set)

for con in inputs:
    a, b = con.split("-")
    connections[a].add(b)
    connections[b].add(a)

sets = set()
def search(node, req):
    key = tuple(sorted(req))
    if key in sets: return
    sets.add(key)
    for n in connections[node]:
        if n in req: continue
        if not req <= connections[n]: continue
        search(n, req | {n})

for x in connections:
    search(x, {x})

print(",".join(max(sets, key=len)))
