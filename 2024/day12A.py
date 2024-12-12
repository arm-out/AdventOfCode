from utils import getInput
from collections import defaultdict

inputs = getInput(12)
inputs = [list(x) for x in inputs]
H = len(inputs)
W = len(inputs[0])

def dfs(r, c, cur):
    global fences

    if (r, c) in cur:
        return

    cur.add((r, c))
    
    plot = inputs[r][c]
    if r+1 < H and inputs[r+1][c] == plot:
        dfs(r+1, c, cur)
    else: fences += 1
    if r-1 >= 0 and inputs[r-1][c] == plot:
        dfs(r-1, c, cur)
    else: fences += 1
    if c+1 < W and inputs[r][c+1] == plot:
        dfs(r, c+1, cur)
    else: fences += 1
    if c-1 >= 0 and inputs[r][c-1] == plot:
        dfs(r, c-1, cur)
    else: fences += 1
    
    return

plots = []
seen = set()
fences = 0
price = 0
for r, row in enumerate(inputs):
    for c, col in enumerate(row):
        if (r, c) not in seen:
            cur = set()
            prev = fences
            dfs(r, c, cur)
            plots.append(cur)
            seen.update(cur)
            perimeter = fences - prev
            area = len(cur)
            price += area * perimeter

print(price)
