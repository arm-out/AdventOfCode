from utils import getInput
from collections import defaultdict

inputs = getInput(11)
stones = inputs[0].split()

for _ in range(25):
    new_stones = []
    for i, s in enumerate(stones):
        if s == '0':
            new_stones.append('1')
        elif len(s) % 2 == 0:
            left = s[:len(s)//2]
            right = s[len(s)//2:]
            new_stones.append(str(int(left)))
            new_stones.append(str(int(right)))
        else:
            new_stones.append(str(int(s) * 2024))
    stones = new_stones

print(len(stones))
