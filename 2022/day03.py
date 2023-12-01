input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
input = input.split('\n')

f = open("inputs/day03.txt", "r")
input = f.read().splitlines()
appears_twice = []

for line in input:
    left = set()
    right = set()

    for i in range(len(line)):
        if (i < (len(line)) / 2):
            left.add(line[i])
        else:
            right.add(line[i])

    common = left.intersection(right)
    appears_twice += list(common)

priority = 0
for char in appears_twice:
    if (ord(char) >= 97):
        priority += ord(char) - 96
    else:
        priority += ord(char) - 38

print(priority)

badges = []
for i in range(0, len(input)-1, 3): 
    l1 = input[i]
    l2 = input[i+1]
    l3 = input[i+2]

    set1 = set()
    set2 = set()
    set3 = set()

    for char in l1:
        set1.add(char)
    for char in l2:
        set2.add(char)
    for char in l3:
        set3.add(char)

    badges += list(set1.intersection(set2, set3))

badge_prio = 0

for char in badges:
    if (ord(char) >= 97):
        badge_prio += ord(char) - 96
    else:
        badge_prio += ord(char) - 38

print(badge_prio)


    

