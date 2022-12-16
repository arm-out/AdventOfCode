f = open("inputs/day08.txt", "r")
input = f.read().splitlines()

cols = len(input[0])
rows = len(input)

visibility = []

def isVisLeft(row, idx):
    size = int(input[row][idx])
    visible = True
    for i in range(0, idx):
        if int(input[row][i]) >= size:
            visible = False
    return visible

def isVisRight(row, idx):
    size = int(input[row][idx])
    visible = True
    for i in range(idx+1, cols):
        if int(input[row][i]) >= size:
            visible = False
    return visible

def isVisUp(row, idx):
    size = int(input[row][idx])
    visible = True
    for i in range(0, row):
        if int(input[i][idx]) >= size:
            visible = False
    return visible

def isVisDown(row, idx):
    size = int(input[row][idx])
    visible = True
    for i in range(row+1, rows):
        if int(input[i][idx]) >= size:
            visible = False
    return visible

visibleTrees = 0
for r in range(rows):
    if (r == 0 or r == rows - 1):
        curRow = [1] * rows
        visibility.append(curRow)
        visibleTrees += sum(x for x in curRow if x == 1)
        continue

    curRow = [-1] * rows
    for c in range(cols):
        if (c == 0 or c == cols - 1):
            curRow[c] = 1
            continue
        if (not (isVisLeft(r, c) or isVisRight(r, c) or isVisUp(r,c) or isVisDown(r,c))):
            curRow[c] = 0
        else:
            curRow[c] = 1
    visibleTrees += sum(x for x in curRow if x == 1)
    visibility.append(curRow)

print(visibleTrees)
