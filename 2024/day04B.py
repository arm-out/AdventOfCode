from utils import getInput

inputs = getInput(4)

ans = 0
for y in range(len(inputs)):
    for x in range(len(inputs[y])):
        if inputs[y][x] != 'A':
            continue

        if y-1 < 0 or y+1 >= len(inputs) or x-1 < 0 or x+1 >= len(inputs[y]):
            continue

        diagonal = 0
        
        # Check \ diagonal MAS
        if inputs[y - 1][x - 1] == 'M' and inputs[y + 1][x + 1] == 'S':
            diagonal += 1

        # Check \ diagonal SAM
        if inputs[y - 1][x - 1] == 'S' and inputs[y + 1][x + 1] == 'M':
            diagonal += 1
        
        # Check / diagonal MAS
        if inputs[y - 1][x + 1] == 'M' and inputs[y + 1][x - 1] == 'S':
            diagonal += 1

        # Check / diagonal SAM
        if inputs[y - 1][x + 1] == 'S' and inputs[y + 1][x - 1] == 'M':
            diagonal += 1

        if diagonal == 2:
            ans += 1

print(ans)


