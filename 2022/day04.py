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
    min1, max1 = int(pair.split(' ')[0]), int(pair.split(' ')[1])
    min2, max2 = int(pair.split(' ')[2]), int(pair.split(' ')[3])
    # p1 = set()
    # p2 = set()

    # for i in range(min1, max1 + 1):
    #     p1.add(i)
    # for i in range(min2, max2 + 1):
    #     p2.add(i)

    if ((min1 <= min2 and max1>= max2) or (min2 <= min1 and max2>= max1)):
        subsets += 1

    if (not (max1 < min2 or max2 < min1)):
        overlap += 1

print(subsets)
print(overlap)
