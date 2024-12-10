from utils import getInput
from collections import defaultdict

inputs = getInput(9)

disk = []
for i, char in enumerate(inputs[0]):
    x = int(char)
    if i % 2 == 0:
        disk += [i // 2] * x
    else:
        disk += [-1] * x

blanks = [i for i, x in enumerate(disk) if x == -1]
for i in blanks:
    while disk[-1] == -1: disk.pop()
    if len(disk) <= i: break
    disk[i] = disk.pop()

# print(disk)
print(sum(i * n for i, n in enumerate(disk)))