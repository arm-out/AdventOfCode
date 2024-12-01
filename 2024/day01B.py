from utils import getInput
from collections import Counter

inputs = getInput(1)
left, right = [], []

for i in inputs:
    l, r = i.split()
    left.append(int(l))
    right.append(int(r))

counts = Counter(right)

cur_sum = 0
for l in left:
    cur_sum += l * counts[l] 

print(cur_sum)
