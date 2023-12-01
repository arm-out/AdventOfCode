f = open("inputs/day08.txt", "r")
input = f.read().splitlines()

cols = len(input[0])
rows = len(input)

scores = []

def scoreLeft(row, idx):
    size = int(input[row][idx])
    score = 0
    for i in range(idx-1, -1, -1):
        if int(input[row][i]) < size:
            score += 1
        else:
            score += 1
            break
    return score

def scoreRight(row, idx):
    size = int(input[row][idx])
    score = 0
    for i in range(idx+1, cols):
        if int(input[row][i]) < size:
            score += 1
        else:
            score += 1
            break
    return score

def scoreUp(row, idx):
    size = int(input[row][idx])
    score = 0
    for i in range(row-1, -1, -1):
        if int(input[i][idx]) < size:
            score += 1
        else:
            score += 1
            break
    return score

def scoreDown(row, idx):
    size = int(input[row][idx])
    score = 0
    for i in range(row+1, rows):
        if int(input[i][idx]) < size:
            score += 1
        else:
            score += 1
            break
    return score

for r in range(rows):
    if (r == 0 or r == rows - 1):
        curRow = [0] * cols
        scores.append(curRow)
        # print(curRow)
        continue

    curRow = [-1] * cols
    for c in range(cols):
        if (c == 0 or c == cols - 1):
            curRow[c] = 0
            continue
        curRow[c] = scoreLeft(r,c) * scoreRight(r,c) * scoreUp(r,c) * scoreDown(r,c)
    scores.append(curRow)
    # print(curRow)

maxScore = 0
for row in scores:
    localMax = max(row)
    maxScore = localMax if localMax > maxScore else maxScore

print(maxScore)



