from utils import getInput
from collections import defaultdict, deque
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

scores = defaultdict(lambda: float('inf'))
prev = defaultdict(set)
min_heap = [(0, start, (0, 1))]

while min_heap:
    s, (r, c), (dr, dc) = heapq.heappop(min_heap)

    directions = [
        (r + dr, c + dc, dr, dc, 1),        # Go straight
        (r - dc, c + dr, -dc, dr, 1001),    # Turn left
        (r + dc, c - dr, dc, -dr, 1001)     # Turn right
    ]
    for nr, nc, cr, cc, cost in directions:
        if inputs[nr][nc] != '#':
            new_score = s + cost
            if new_score < scores[(nr, nc, cr, cc)]:
                scores[(nr, nc, cr, cc)] = new_score
                heapq.heappush(min_heap, (new_score, (nr, nc), (cr, cc)))
                prev[(nr, nc, cr, cc)] = {(r, c, dr, dc)}
            elif new_score == scores[(nr, nc, cr, cc)]:
                heapq.heappush(min_heap, (new_score, (nr, nc), (cr, cc)))
                prev[(nr, nc, cr, cc)].add((r, c, dr, dc))


# print(prev)

end_dirs = []
min_score = float('inf')
for r, c, dr, dc in scores:
    if (r, c) != end:
        continue
    if scores[(r, c, dr, dc)] < min_score:
        end_dirs = [(r, c, dr, dc)]
        min_score = scores[(r, c, dr, dc)]
    elif scores[(r, c, dr, dc)] == min_score:
        end_dirs.append((r, c, dr, dc))

q = deque(end_dirs)
path = set()
while q:
    r, c, dr, dc = q.popleft()
    path.add((r, c))
    q.extend(prev[(r, c, dr, dc)])

print(len(path))



    