from utils import getInput
from collections import defaultdict

inputs = getInput(5)

pivot = inputs.index('')
rules = inputs[:pivot]
updates = inputs[pivot+1:]

rule_table = defaultdict(list)
for rule in rules:
    parts = rule.split('|')
    rule_table[parts[0].strip()].append(parts[1].strip())

correct = []
for update in updates:
    pages = update.split(',')
    so_far = []
    for i, p in enumerate(pages):
        prereqs = rule_table[p]
        if any(x in so_far for x in prereqs):
            break
        
        so_far.append(pages[i])
        if i == len(pages) - 1:
            correct.append(update)

ans = 0
for c in correct:
    ps = c.split(',')
    ans += int(ps[len(ps)//2])

print(ans)
    

    
    



