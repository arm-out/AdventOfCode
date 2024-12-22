from utils import getInput
from collections import deque, defaultdict

inputs = getInput(22)
secrets = list(map(int, inputs))

def step(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num

buy = defaultdict(int)

for i, n in enumerate(secrets):
    prices = deque([n % 10])
    seen = set()
    for _ in range(2000):
        secrets[i] = step(secrets[i])
        prices.append(secrets[i] % 10)
        if len(prices) >= 5:
            a, b, c, d, e = prices
            seq = (b-a, c-b, d-c, e-d)
            prices.popleft()
            if seq in seen: continue
            seen.add(seq)
            buy[seq] += e

# print(secrets)
print(max(buy.values()))

