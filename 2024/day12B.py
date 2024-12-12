from utils import getInput
from collections import defaultdict

inputs = getInput(12)
inputs = [list(x) for x in inputs]
H = len(inputs)
W = len(inputs[0])

def dfs(r, c, cur, edges):
    if (r, c) in cur:
        return

    cur.add((r, c))
    plot = inputs[r][c]

    if r+1 < H and inputs[r+1][c] == plot:
        dfs(r+1, c, cur, edges)
    else: edges.add((r, c, 'down'))
    if r-1 >= 0 and inputs[r-1][c] == plot:
        dfs(r-1, c, cur, edges)
    else: edges.add((r, c, 'up')) 
    if c+1 < W and inputs[r][c+1] == plot:
        dfs(r, c+1, cur, edges)
    else: edges.add((r, c, 'right')) 
    if c-1 >= 0 and inputs[r][c-1] == plot:
        dfs(r, c-1, cur, edges)
    else: edges.add((r, c, 'left'))

def getSides(edges):
    seen = set()
    sides = 0
    for edge in edges:
        if edge in seen: continue
        sides += 1
        r, c, side = edge
        if side == 'up':
            for dc in [-1, 1]:
                next_edge = (r, c + dc, 'up')
                while next_edge in edges:
                    seen.add(next_edge)
                    nr, nc, _ = next_edge
                    next_edge = (nr, nc + dc, 'up')
        elif side == 'down':
            for dc in [-1, 1]:
                next_edge = (r, c + dc, 'down')
                while next_edge in edges:
                    seen.add(next_edge)
                    nr, nc, _ = next_edge
                    next_edge = (nr, nc + dc, 'down')
        elif side == 'left':
            for dr in [-1, 1]:
                next_edge = (r + dr, c, 'left')
                while next_edge in edges:
                    seen.add(next_edge)
                    nr, nc, _ = next_edge
                    next_edge = (nr + dr, nc, 'left')   
        elif side == 'right':
            for dr in [-1, 1]:
                next_edge = (r + dr, c, 'right')
                while next_edge in edges:
                    seen.add(next_edge)
                    nr, nc, _ = next_edge
                    next_edge = (nr + dr, nc, 'right')
    return sides

seen = set()
price = 0
for r, row in enumerate(inputs):
    for c, col in enumerate(row):
        if (r, c) not in seen:
            cur = set()
            edges = set()
            dfs(r, c, cur, edges)
            seen.update(cur)
            sides = getSides(edges)
            area = len(cur)
            price += area * sides

print(price)
