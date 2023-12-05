from utils import getInput
from functools import reduce

DAY = 6
getInput(DAY)

f = open("inputs/day06.txt", "r")
input = f.read().splitlines()

times = list(map(int, input[0].split(":")[1].split()))
distance = list(map(int, input[1].split(":")[1].split()))

print(times)
print(distance)

win = [0 for _ in range(len(times))]

for i in range(len(times)):
    for time in range(times[i]):
        if (times[i] - time) * time > distance[i]:
            win[i] += 1

print(reduce(lambda x, y: x * y, win, 1))