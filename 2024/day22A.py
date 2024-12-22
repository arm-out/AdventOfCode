from utils import getInput

inputs = getInput(22)
secrets = list(map(int, inputs))

def step(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num

for _ in range(2000):
    for i, n in enumerate(secrets):
        secrets[i] = step(n)

# print(secrets)
print(sum(secrets))

