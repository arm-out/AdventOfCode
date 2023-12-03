f = open("inputs/day04.txt", "r")
input = f.read().splitlines()

total = 0
for line in input:
    card = line.split(":")
    winning = card[1].split("|")[0].split(" ")
    winning = [int(x) for x in winning if x.isnumeric()]
    numbers = card[1].split("|")[1].split(" ")
    numbers = [int(x) for x in numbers if x.isnumeric()]

    score = 0
    for num in numbers:
        if num in winning:
            if score == 0:
                score = 1
            else:
                score *= 2
    
    total += score

print(total)
