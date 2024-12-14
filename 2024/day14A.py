from utils import getInput
from math import prod

inputs = getInput(14)
H = 103
W = 101
time = 100

final_pos = []
for line in inputs:
    p_text, v_text = line.split(' ')
    p = list(map(int, p_text.split('=')[1].split(',')))
    v = list(map(int, v_text.split('=')[1].split(',')))
    
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

print(prod(quadrants))
