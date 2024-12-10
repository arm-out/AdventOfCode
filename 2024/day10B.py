from utils import getInput
from collections import defaultdict

inputs = getInput(10)
inputs = [list(x) for x in inputs]
H = len(inputs)
W = len(inputs[0])

origins = []
for r in range(H):
    for c in range(W):
        if inputs[r][c] == '0':
            origins.append((r, c))

def dfs(r, c, cur):
    if r < 0 or r >= H or c < 0 or c >= W:
        return 0
    if cur == 9:
        return 1

    left, right, up, down = 0, 0, 0, 0
    if c > 0 and inputs[r][c-1] == str(cur + 1):
        left = dfs(r, c-1, cur + 1)
    if c < W - 1 and inputs[r][c+1] == str(cur + 1):
        right = dfs(r, c+1, cur + 1)
    if r > 0 and inputs[r-1][c] == str(cur + 1):
        up = dfs(r-1, c, cur + 1)
    if r < H - 1 and inputs[r+1][c] == str(cur + 1):
        down = dfs(r+1, c, cur + 1)
    
    return left + right + up + down

res = []
for origin in origins:
    res.append(dfs(origin[0], origin[1], 0))

print(sum(res))
    
