from utils import getInput

inputs = getInput(19)
towels = inputs[0].split(', ')
patterns = inputs[2:]

def search(pat):
    if pat == '':
        return True
    
    for towel in towels:
        if pat.startswith(towel):
            if search(pat[len(towel):]):
                return True
    
    return False

res = 0
for p in patterns:
    if search(p):
        res += 1

print(res)