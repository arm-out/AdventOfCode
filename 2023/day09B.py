from utils import getInput

inputs = getInput(9)

history = []
for line in inputs:
    line = list(map(int, line.split()))
    line.reverse()
    difs = [line]
    while not all(x == 0 for x in difs[-1]):
        curr = []
        for i in range(1, len(difs[-1])):
            curr.append(difs[-1][i] - difs[-1][i-1])
        difs.append(curr)

    difs.reverse()
    difs[0].append(0)
    for i in range(1, len(difs)):
        difs[i].append(difs[i-1][-1] + difs[i][-1])

    # print(difs)
    history.append(difs[-1][-1])

# print(history)
print(sum(history))