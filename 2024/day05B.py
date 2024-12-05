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
incorrect = []
for update in updates:
    pages = update.split(',')
    so_far = []
    for i, p in enumerate(pages):
        prereqs = rule_table[p]
        if any(x in so_far for x in prereqs):
            incorrect.append(update)
            break
        
        so_far.append(pages[i])
        if i == len(pages) - 1:
            correct.append(update)

ans = []
for c in incorrect:
    pages = c.split(',')

    i = 0
    while i < len(pages):

        prereqs = rule_table[pages[i]]
        while any(x in pages[:i] for x in prereqs):
            p = pages.pop(i)
            pages.insert(0, p)
            i = 0
        i += 1
    
    ans.append(pages)

ans_sum = 0
for a in ans:
    ans_sum += int(a[len(a)//2])

print(ans_sum)