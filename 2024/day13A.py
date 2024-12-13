from utils import getInput
import numpy as np

inputs = getInput(13)
cost = 0
for i in range(0, len(inputs), 4):
    a_line = inputs[i]
    b_line = inputs[i + 1]
    prize_line = inputs[i + 2]
    
    xa = a_line[a_line.index('X') + 2 : a_line.index(',')]
    ya = a_line[a_line.index('Y') + 2 :]
    xb = b_line[b_line.index('X') + 2 : b_line.index(',')]
    yb = b_line[b_line.index('Y') + 2 :]
    px = prize_line[prize_line.index('X') + 2 : prize_line.index(',')]
    py = prize_line[prize_line.index('Y') + 2 :]
    xa, ya, xb, yb, px, py = map(int, [xa, ya, xb, yb, px, py])

    p = np.array([px, py])
    system = np.matrix([[xa, xb], [ya, yb]])
    res = np.linalg.solve(system, p)

    if np.allclose(res, np.round(res)):
        cost += (res[0] * 3) + res[1]

print(int(cost))