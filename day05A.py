from collections import deque

f = open("inputs/day05.txt", "r")
input = f.read().splitlines()

delim_idx = -1
for i in range(len(input)):
    if (len(input[i]) == 0):
        delim_idx = i
        break

# Setup
stack_names = input[delim_idx-1]
stacks = []
for i in range(len(stack_names)):
    if (stack_names[i] == ' '):
        continue
    
    cur_stack = deque()
    for row in range(delim_idx-2, -1, -1):
        if (input[row][i] == ' '):
            break
        cur_stack.append(input[row][i])

    stacks.append(cur_stack)

# Moves
for i in range(delim_idx + 1, len(input)):
    row = input[i].split(' ')
    count = int(row[1])
    from_stack = int(row[3]) - 1
    dest_stack = int(row[5]) - 1

    for j in range(count):
        crate = stacks[from_stack].pop()
        stacks[dest_stack].append(crate)

result = ''
for stack in stacks:
    result += stack[-1]

print(result)

