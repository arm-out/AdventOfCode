from utils import getInput
from collections import defaultdict

inputs = getInput(7)
res = set()
for line in inputs:
    total = line.split(":")[0]
    parts = line.split(":")[1].split(" ")[1:]
    total = int(total)
    parts = [int(x) for x in parts]

    def backtrack(i, cur, res):
        if cur == total:
            print(cur)
            res.add(cur)
            return
        if i >= len(parts):
            return

        # * op
        cur *= parts[i]
        backtrack(i+1, cur, res)
        cur //= parts[i]
        # + op
        cur += parts[i]
        backtrack(i+1, cur, res)
        cur -= parts[i]

    backtrack(1, parts[0], res)

print(sum(list(res)))