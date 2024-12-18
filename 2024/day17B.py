from utils import getInput

inputs = getInput(17)
inputs = [x.split() for x in inputs]
program = list(map(int, inputs[-1][-1].split(',')))

# 24: b = a % 8
# 12: b = b ^ 2
# 75: c = a >> b
# 47: b = b ^ c
# 13: b = b ^ 3
# 55: out(b % 8)
# 03: a = a >> 3
# 30: if a != 0: jump 0

def search(prog, ans):
    if prog == []:
        return ans
    for b in range(8):
        a = ans << 3 | b
        b = b ^ 2
        c = a >> b
        b = b ^ c
        b = b ^ 3
        if b % 8 == prog[-1]:
            sub = search(prog[:-1], a)
            if sub is not None:
                return sub

print(search(program, 0))
