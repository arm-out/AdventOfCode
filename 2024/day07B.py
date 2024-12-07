from utils import getInput
from collections import defaultdict

inputs = getInput(7)
res = 0

for line in inputs:
    total = int(line.split(":")[0])
    parts = [int(x) for x in line.split(":")[1].split(" ")[1:]]

    def backtrack(i, cur):
        if i == len(parts):
            return cur == total

        # Addition
        if backtrack(i + 1, cur + parts[i]):
            return True
        
        # Multiplication
        if backtrack(i + 1, cur * parts[i]):
            return True
        
        # Concatenation
        concat = int(str(cur) + str(parts[i]))
        if backtrack(i + 1, concat):
            return True
        
        return False

    if backtrack(1, parts[0]):
        res += total

print(res)