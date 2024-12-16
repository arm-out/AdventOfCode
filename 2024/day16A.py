from utils import getInput
import heapq

inputs = getInput(16)
inputs = [list(x) for x in inputs]
H = len(inputs)
W = len(inputs[0])

start = None
end = None
for r in range(H):
    for c in range(W):
        if inputs[r][c] == 'S':
            start = (r, c)
        elif inputs[r][c] == 'E':
            end = (r, c)
        if start and end:
            break
    else:
        continue
    break

scores = {}
min_heap = [(0, start, (0, 1))]

while min_heap:
    s, (r, c), (dr, dc) = heapq.heappop(min_heap)
    if (r, c) in scores:
        continue
    else:
        scores[(r, c)] = s

    # Go straight
    nr, nc = r + dr, c + dc
    if inputs[nr][nc] != '#' and (nr, nc) not in scores:
        heapq.heappush(min_heap, (s + 1, (nr, nc), (dr, dc)))
    # Turn left
    cr, cc = -dc, dr
    nr, nc = r + cr, c + cc
    if inputs[nr][nc] != '#' and (nr, nc) not in scores:
        heapq.heappush(min_heap, (s + 1001, (nr, nc), (cr, cc)))
    # Turn right
    cr, cc = dc, -dr
    nr, nc = r + cr, c + cc
    if inputs[nr][nc] != '#' and (nr, nc) not in scores:
        heapq.heappush(min_heap, (s + 1001, (nr, nc), (cr, cc)))

print(scores[end])

    