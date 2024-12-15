from utils import getInput

inputs = getInput(15)
grid = []
move_list = []
for i, line in enumerate(inputs):
    if len(line) == 0:
        break
    grid.append(list(line))

for row in range(i + 1, len(inputs)):
    move_list.append(inputs[row])

dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

robot = None
wide_grid = []
for r, row in enumerate(grid):
    wide_row = []
    for c, col in enumerate(row):
        if col == '#':
            wide_row.extend(['#', '#'])
        elif col == 'O':
            wide_row.extend(['[', ']'])
        elif col == '.':
            wide_row.extend(['.', '.'])
        elif col == '@':
            robot = (r, len(wide_row))
            wide_row.extend(['@', '.'])
    wide_grid.append(wide_row)
grid = wide_grid
# print(grid)
# print(move_list)

for moves in move_list:
    for move in moves:
        dr, dc = dirs[move]
        targets = [robot]
        go = True
        for cr, cc in targets:
            nr, nc = cr + dr, cc + dc
            if (nr, nc) in targets: continue
            if grid[nr][nc] == '#':
                go = False
                break
            if grid[nr][nc] == '[':
                targets.append((nr, nc))
                targets.append((nr, nc + 1))
            if grid[nr][nc] == ']':
                targets.append((nr, nc))
                targets.append((nr, nc - 1))
        if not go: continue
        copy = [list(row) for row in grid]
        grid[robot[0]][robot[1]] = '.'
        grid[robot[0] + dr][robot[1] + dc] = '@'
        for r, c in targets[1:]:
            grid[r][c] = '.'
        for r, c in targets[1:]:
            grid[r + dr][c + dc] = copy[r][c]
        
        robot = (robot[0] + dr, robot[1] + dc)

res = 0
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == '[':
            res += 100 * r + c

print(res)
        