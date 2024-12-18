from utils import getInput
from collections import deque

inputs = getInput(18)
inputs =[list(map(int, x.split(','))) for x in inputs]
dim = 71

def bfs(n):
    grid = [['.' for _ in range(dim)] for _ in range(dim)]
    for r, c in inputs[:n]:
        grid[r][c] = '#'

    q = deque()
    seen = set([(0, 0)])
    prev = {(0,0): None}
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        if (r, c) == (dim-1, dim-1):
            return True
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < dim and 0 <= nc < dim and grid[nr][nc] != '#' and (nr, nc) not in seen:
                seen.add((nr, nc))
                prev[(nr, nc)] = (r, c)
                q.append((nr, nc))

l, r = 0, len(inputs) - 1
while l <= r:
    mid = (l + r) // 2
    if bfs(mid + 1):
        l = mid + 1
    else:
        r = mid - 1

print(inputs[max(l, r)])
