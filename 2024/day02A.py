from utils import getInput

inputs = getInput(2)

safe = 0
for line in inputs:
    levels = line.split()
    levels = [int(l) for l in levels]
    is_increasing = True
    for i, l in enumerate(levels):
        if i == 0 and l < levels[i+1]:
            is_increasing = True
            continue
        elif i == 0 and l > levels[i+1]:
            is_increasing = False
            continue

        if is_increasing and (l - levels[i-1] < 1 or l - levels[i-1] > 3):
            break
            
        if not is_increasing and (l - levels[i-1] > -1 or l - levels[i-1] < -3):
            break

        if i == len(levels) - 1:
            safe += 1
    
print(safe)