from utils import getInput
from functools import cmp_to_key

inputs = getInput(5)
rules = []
updates = []

done_rules = False
for line in inputs:
    if len(line) == 0:
        done_rules = True
        continue
    if not done_rules: rules.append(list(map(int, line.split('|'))))
    if done_rules: updates.append(list(map(int, line.split(','))))

cache = {}

for x, y in rules:
    cache[(x, y)] = -1
    cache[(y, x)] = 1

def isOrdered(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            key = (update[i], update[j])
            if key in cache and cache[key] == 1:
                return False
    return True

def cmp(x,y):
    return cache[(x,y)]

total = 0
for update in updates:
    if isOrdered(update): continue
    update.sort(key=cmp_to_key(cmp))
    total += update[len(update)//2]

print(total)