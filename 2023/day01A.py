f = open("inputs/day01.txt", "r")
input = f.read().splitlines()

nums = []
for line in input:
    first = ''
    last = ''
    for i in range(len(line)):
        if (line[i].isnumeric() and first == ''):
            first = line[i]
        elif (line[i].isnumeric()):
            last = line[i] 

    nums.append(int(first + (last or first)))

print(sum(nums))