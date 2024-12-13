from utils import getInput

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
    ax, ay, bx, by, px, py = map(int, [xa, ya, xb, yb, px, py])

    px += 10000000000000
    py += 10000000000000
    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx

    if ca % 1 == cb % 1 == 0:
        cost += int(ca * 3 + cb)

print(cost)