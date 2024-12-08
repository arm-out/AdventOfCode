from utils import getInput
from collections import defaultdict

inputs = getInput(8)

freq = defaultdict(list)
grid = [list(x) for x in inputs]
H, W = len(grid), len(grid[0])

for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if row[x] != '.':
            freq[row[x]].append((y,x))

antinodes = [[0] * W for _ in range(H)]
for nodes in freq:
    node_list = freq[nodes]
    for node in node_list:
        for other in node_list:
            if node == other:
                continue        
            y1, x1 = node
            y2, x2 = other
            dy, dx = y2-y1, x2-x1
            posy, posx = y1-dy, x1-dx
            antinodes[y1][x1] += 1

            while 0 <= posy < H and 0 <= posx < W:
                antinodes[posy][posx] += 1
                posy -= dy
                posx -= dx

res = 0
for a_row in antinodes:
    for val in a_row:
        if val > 0:
            res += 1
print(res)