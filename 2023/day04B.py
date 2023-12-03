import bisect

f = open("inputs/day04.txt", "r")
input = f.read().splitlines()


copies = [1 for _ in range(len(input))]
for i in range(len(input)):
    line = input[i]
    card = line.split(":")
    winning = card[1].split("|")[0].split(" ")
    winning = [int(x) for x in winning if x.isnumeric()]
    numbers = card[1].split("|")[1].split(" ")
    numbers = [int(x) for x in numbers if x.isnumeric()]

    matches = 0
    for num in numbers:
        if num in winning: matches += 1
    
    for c in range(matches):
        copies[i+c+1] += copies[i]

print(copies)
print(sum(copies))
