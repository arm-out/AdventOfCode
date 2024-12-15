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
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == '@':
            robot = (r, c)
            break

def move_piece(pos, direction):
    next_move = (pos[0] + direction[0], pos[1] + direction[1])
    if grid[next_move[0]][next_move[1]] == '#':
        return False
    if grid[next_move[0]][next_move[1]] == '.':
        grid[next_move[0]][next_move[1]] = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = '.'
        return True
    if grid[next_move[0]][next_move[1]] == 'O':
        if (move_piece(next_move, direction)):
            return move_piece(pos, direction)
        return False

for moves in move_list:
    for move in moves:
        direction = dirs[move]
        next_move = (robot[0] + direction[0], robot[1] + direction[1])
        if move_piece(robot, direction):
            robot = next_move

res = 0
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == 'O':
            res += 100 * r + c

print(res)
        