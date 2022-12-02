strats = open("inputs/day02.txt", "r")

win = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
}

points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

score1 = 0
score2 = 0

for line in strats:
    moves = line.split()
    # win
    if (moves[0] == win[moves[1]]):
        score1 += points[moves[1]] + 6
    # draw
    elif (ord(moves[0]) + 23 == ord(moves[1])):
        score1 += points[moves[1]] + 3
    # loss
    else:
        score1 += points[moves[1]]

print(score1)

lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

win2 = dict([(value, key) for key, value in win.items()])

strats.seek(0)

for line in strats:
    moves = line.split()
    # win
    match moves[1]:
        case 'Z':
            score2 += points[win2[moves[0]]] + 6
        case 'Y':
            score2 += points[chr(ord(moves[0])+23)] + 3
        case 'X':
            score2 += points[lose[moves[0]]]

print(score2)
