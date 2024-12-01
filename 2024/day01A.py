from utils import getInput

inputs = getInput(1)
left, right = [], []

for i in inputs:
    l, r = i.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

distance = 0
for l, r in zip(left, right):
    distance += abs(l - r)

print(distance)
