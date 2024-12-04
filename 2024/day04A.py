from utils import getInput

inputs = getInput(4)

ans = 0
for y in range(len(inputs)):
    for x in range(len(inputs[y])):
        if inputs[y][x] != 'X':
            continue

        # Check down
        if y + 3 < len(inputs) and inputs[y + 1][x] == 'M' and inputs[y + 2][x] == 'A' and inputs[y + 3][x] == 'S':
            ans += 1
        
        # Check right
        if x + 3 < len(inputs[y]) and inputs[y][x + 1] == 'M' and inputs[y][x + 2] == 'A' and inputs[y][x + 3] == 'S':
            ans += 1
        
        # Check down-right
        if x + 3 < len(inputs[y]) and y + 3 < len(inputs) and inputs[y + 1][x + 1] == 'M' and inputs[y + 2][x + 2] == 'A' and inputs[y + 3][x + 3] == 'S':
            ans += 1
        
        # Check down-left
        if x - 3 >= 0 and y + 3 < len(inputs) and inputs[y + 1][x - 1] == 'M' and inputs[y + 2][x - 2] == 'A' and inputs[y + 3][x - 3] == 'S':
            ans += 1

        # Check left
        if x - 3 >= 0 and inputs[y][x - 1] == 'M' and inputs[y][x - 2] == 'A' and inputs[y][x - 3] == 'S':
            ans += 1
        
        # Check up-left
        if x - 3 >= 0 and y - 3 >= 0 and inputs[y - 1][x - 1] == 'M' and inputs[y - 2][x - 2] == 'A' and inputs[y - 3][x - 3] == 'S':
            ans += 1
        
        # Check up
        if y - 3 >= 0 and inputs[y - 1][x] == 'M' and inputs[y - 2][x] == 'A' and inputs[y - 3][x] == 'S':
            ans += 1
        
        # Check up-right
        if x + 3 < len(inputs[y]) and y - 3 >= 0 and inputs[y - 1][x + 1] == 'M' and inputs[y - 2][x + 2] == 'A' and inputs[y - 3][x + 3] == 'S':
            ans += 1

print(ans)


