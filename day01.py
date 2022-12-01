f = open("inputs/day01.txt", "r")

calories = []

acc = 0
for line in f:
    if (line != '\n'):
        acc += int(line)
    else:
        calories.append(acc)
        acc = 0

calories.sort(reverse=True)
print(calories[0])

print(sum(calories[0:3]))
