f = open("inputs/day03.txt", "r")
input = f.read().splitlines()

# setup
for i in range(len(input)):
    input[i] = list(input[i])

def getNums(i, j):
    if i < 0 or i >= len(input):
        return 0
    if j < 0 or j >= len(input[i]):
        return 0

    if not input[i][j].isnumeric():
        return 0
    
    curr = input[i][j]
    l = j-1
    r = j+1
    
    # scan left
    while l >= 0 and input[i][l].isnumeric():
        curr = input[i][l] + curr
        input[i][l] = "."
        l -= 1

    # scan right
    while r < len(input[i]) and input[i][r].isnumeric():
        curr += input[i][r]
        input[i][r] = "."
        r += 1

    return int(curr)

gears = []
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "*":
            gear_parts = []
            gear_parts.append(getNums(i-1, j)) # up
            gear_parts.append(getNums(i+1, j)) # down
            gear_parts.append(getNums(i, j-1)) # left
            gear_parts.append(getNums(i, j+1)) # right
            gear_parts.append(getNums(i-1, j-1)) # up-left
            gear_parts.append(getNums(i-1, j+1)) # up-right
            gear_parts.append(getNums(i+1, j-1)) # down-left
            gear_parts.append(getNums(i+1, j+1)) # down-right

            print(gear_parts)
            gear_parts = [x for x in gear_parts if x != 0]
            print(gear_parts)
            if len(gear_parts) == 2:
                gears.append(gear_parts[0] * gear_parts[1])
            

print(sum(gears))