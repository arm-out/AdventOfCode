from utils import getInput
from collections import defaultdict

inputs = getInput(7)

def can_obtain(target, array):
    if len(array) == 1: return target == array[0]
    if target % array[-1] == 0 and can_obtain(target // array[-1], array[:-1]): return True
    if target > array[-1] and can_obtain(target - array[-1], array[:-1]): return True
    s_target = str(target)
    s_last = str(array[-1])
    if len(s_target) > len(s_last) and s_target.endswith(s_last) and can_obtain(int(s_target[:-len(s_last)]), array[:-1]): return True
    return False

res = 0
for line in inputs:
    left, right = line.split(":")
    total = int(left)
    parts = [int(x) for x in right.split()]
    if can_obtain(total, parts):
        res += total
    
print(res)