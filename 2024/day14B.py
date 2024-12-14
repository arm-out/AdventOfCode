from utils import getInput
from math import prod

inputs = getInput(14)
H = 103
W = 101

robots = []
for line in inputs:
    p_text, v_text = line.split(' ')
    p = list(map(int, p_text.split('=')[1].split(',')))
    v = list(map(int, v_text.split('=')[1].split(',')))
    robots.append((p, v))

min_sf = float('inf')
best_iter = None
for time in range(H * W):
    final_pos = []
    for p, v in robots:
        pos = ((p[0] + v[0] * time) % W, (p[1] + v[1] * time) % H)
        final_pos.append(pos)

    quadrants = [0, 0, 0, 0]
    for pos in final_pos:
        if pos[0] < W // 2 and pos[1] < H // 2:
            quadrants[0] += 1
        elif pos[0] > W // 2 and pos[1] < H // 2:
            quadrants[1] += 1
        elif pos[0] < W // 2 and pos[1] > H // 2:
            quadrants[2] += 1
        elif pos[0] > W // 2 and pos[1] > H // 2:
            quadrants[3] += 1

    sf = prod(quadrants)
    if sf < min_sf:
        min_sf = sf
        best_iter = time

print(min_sf, best_iter)

