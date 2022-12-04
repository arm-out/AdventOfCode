input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
input = input.split('\n')

f = open("inputs/day04.txt", "r")
input = f.read().splitlines()

for i in range(len(input)):
    input[i] = input[i].replace('-', ' ')
    input[i] = input[i].replace(',', ' ')

subsets = 0
overlap = 0

for pair in input:
    p1_start, p1_end = int(pair.split(' ')[0]), int(pair.split(' ')[1])
    p2_start, p2_end = int(pair.split(' ')[2]), int(pair.split(' ')[3])
    p1 = set()
    p2 = set()

    for i in range(p1_start, p1_end + 1):
        p1.add(i)
    for i in range(p2_start, p2_end + 1):
        p2.add(i)

    if (p1.issubset(p2) or p2.issubset(p1)):
        subsets += 1

    if (len(p1.intersection(p2)) != 0):
        overlap += 1

print(subsets)
print(overlap)
