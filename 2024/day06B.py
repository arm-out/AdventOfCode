from utils import getInput
from collections import defaultdict

inputs = getInput(6)
grid = [list(x) for x in inputs]
rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '^': break
    else:
        continue
    break

path = set()
def loops(r, c, initial=False):
    dr = -1
    dc = 0
    visited = set()

    while True:
        visited.add((r, c, dr, dc))
        if initial: path.add((r, c))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
            return False
        if grid[r + dr][c + dc] == '#':
            dc, dr = -dr, dc
        else:
            c += dc
            r += dr
        if (r, c, dr, dc) in visited:
            return True

# get initial path
loops(r, c, True)
total = 0
for p in path:
    if grid[p[0]][p[1]] == '^': continue
    grid[p[0]][p[1]] = '#'
    if loops(r, c):
        total += 1
    grid[p[0]][p[1]] = '.'

print(total)
