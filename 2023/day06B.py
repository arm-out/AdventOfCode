from utils import getInput

DAY = 6
getInput(DAY)

f = open("inputs/day06.txt", "r")
input = f.read().splitlines()

time = int(''.join(input[0].split(":")[1].split()))
distance = int(''.join(input[1].split(":")[1].split()))

print(time)
print(distance)

upper = 0
lower = 0

for i in range(time):
    if (time - i) * i > distance:
        lower = i
        break

for i in range(time, 0, -1):
    if (time - i) * i > distance:
        upper = i
        break

print(upper - lower + 1)
