from utils import getInput
from collections import defaultdict

inputs = getInput(6)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

inputs = [list(x) for x in inputs]

pos = (0, 0)
for r, row in enumerate(inputs):
    for c, col in enumerate(row):
        if col == '^':
            pos = (r, c)

dir_idx = 0 % 4
while 0 <= pos[0] < len(inputs) and 0 <= pos[1] < len(inputs[0]):
    cur_dir = dirs[dir_idx]
    next_pos = (pos[0] + cur_dir[0], pos[1] + cur_dir[1])
    if next_pos[0] < 0 or next_pos[0] >= len(inputs) or next_pos[1] < 0 or next_pos[1] >= len(inputs[0]):
        break
    if inputs[next_pos[0]][next_pos[1]] == '#':
        dir_idx = (dir_idx + 1) % 4
    else:
        inputs[pos[0]][pos[1]] = 'X'
        pos = next_pos

ans = 0
for row in inputs:
    for col in row:
        if col == 'X':
            ans += 1
print(ans)
