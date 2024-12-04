from utils import getInput

inputs = getInput(3)

ans = 0
for line in inputs:
    for i in range(len(line)):
        if line[i:i+4] == 'mul(':
            closing = line.find(')', i)
            if closing == -1:
                continue
            
            param_string = line[i+4:closing]
            if " " in param_string:
                continue

            params = line[i+4:closing].split(',')

            if len(params) != 2 or (not params[0].isdigit() or not params[1].isdigit()):
                continue

            ans += int(params[0]) * int(params[1])

print(ans)

