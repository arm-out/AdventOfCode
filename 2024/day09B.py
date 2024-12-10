from utils import getInput
from collections import defaultdict

inputs = getInput(9)

disk = {}
blanks = []
pos = 0
for i, char in enumerate(inputs[0]):
    x = int(char)
    if i % 2 == 0:
        disk[i // 2] = (pos, x)
    else:
        blanks.append((pos, x))
    pos += x

fid = len(disk) - 1
while fid > 0:
    pos, size = disk[fid]
    for i, (start, length) in enumerate(blanks):
        if start >= pos:
            blanks = blanks[:i]
            break
        if length >= size:
            disk[fid] = (start, size)
            if length == size:
                blanks.pop(i)
            else:
                blanks[i] = (start + size, length - size)
            break
    fid -= 1

total = 0
for fid, (pos, size) in disk.items():
    for i in range(pos, pos + size):
        total += fid * i

# print(blanks)
# print(disk)
print(total)