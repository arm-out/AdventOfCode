from utils import getInput

inputs = getInput(20)
track = [list(x) for x in inputs]
H = len(track)
W = len(track[0])

for r in range(H):
    for c in range(W):
        if track[r][c] == 'S':
            break
    else:
        continue
    break

dists = [[-1] * W for _ in range(H)]
dists[r][c] = 0

while track[r][c] != 'E':
    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if nr < 0 or nr >= H or nc < 0 or nc >= W: continue
        if track[nr][nc] == '#': continue
        if dists[nr][nc] != -1: continue
        dists[nr][nc] = dists[r][c] + 1
        r, c = nr, nc

count = 0
for i in range(H):
    for j in range(W):
        if track[i][j] == '#': continue
        for ni, nj in [(i-1, j+1), (i, j+2), (i+1, j+1), (i+2, j)]:
            if ni < 0 or ni >= H or nj < 0 or nj >= W: continue
            if track[ni][nj] == '#': continue
            if abs(dists[i][j] - dists[ni][nj]) >= 102: count += 1

print(count)
