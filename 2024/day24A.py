from utils import getInput
from collections import defaultdict, deque

inputs = getInput(24)
wires = defaultdict(int)
gates = deque()
for i, line in enumerate(inputs):
    if line == "": break
    x, val = line.split(":")
    wires[x] = int(val)

for ins in inputs[i+1:]:
    a, op, b, _, x = ins.split()
    gates.append((a, op, b, x))

while gates:
    a, op, b, x = gates.popleft()
    if a not in wires or b not in wires:
        gates.append((a, op, b, x))
        continue
    
    if op == "AND":
        wires[x] = wires[a] & wires[b]
    elif op == "OR":
        wires[x] = wires[a] | wires[b]
    elif op == "XOR":
        wires[x] = wires[a] ^ wires[b]

val = []
for w in wires:
    if w.startswith("z"):
        val.append(w)

print(int("".join([str(wires[x]) for x in sorted(val, reverse=True)]), 2))

