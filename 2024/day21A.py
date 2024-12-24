from utils import getInput

inputs = getInput(21)

num_coords = {
    '7': (0,0), '8': (0,1), '9': (0,2),
    '4': (1,0), '5': (1,1), '6': (1,2),
    '1': (2,0), '2': (2,1), '3': (2,2),
                '0': (3,1), 'A': (3,2)
}

def coords_to_code(dirs):
    commands = []
    for (y, x) in dirs:
        cur = ''
        if y < 0:
            cur += '^' * abs(y)
        else:
            cur += 'v' * abs(y)
        if x < 0:
            cur += '<' * abs(x)
        else:
            cur += '>' * abs(x)
        commands.append(cur)
        commands.append('A')
    return "".join(commands)

def num_to_coords(code):
    dirs = []
    cur = num_coords['A']
    for c in code:
        target = num_coords[c]
        dirs.append((target[0] - cur[0], target[1] - cur[1]))
        cur = target
    return dirs

arrow_coords = {
                '^': (0,1), 'A': (0,2),
    '<': (1,0), 'v': (1,1), '>': (1,2)
}

def arrow_to_coords(code):
    dirs = []
    cur = arrow_coords['A']
    for c in code:
        target = arrow_coords[c]
        dirs.append((target[0] - cur[0], target[1] - cur[1]))
        cur = target

    return dirs

res = 0
for i in inputs:
    dir1 = num_to_coords(i)
    code1 = coords_to_code(dir1)
    dir2 = arrow_to_coords(code1)
    code2 = coords_to_code(dir2)
    dir3 = arrow_to_coords(code2)
    code3 = coords_to_code(dir3)
    if i == '379A':
        print(code1)
        print(code2)
        print(code3)
    print(len(code3), int(i[:len(i) - 1])) 
    res += len(code3) * int(i[:len(i) - 1])

print(res)
