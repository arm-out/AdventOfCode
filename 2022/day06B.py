f = open("inputs/day06.txt", "r")
input = f.read().splitlines()

def startOfMessage(input):
    for i in range(len(input)):
        code = set([input[x] for x in range(i, i+14) ])
        if (len(code) == 14):
            return i+14

print(startOfMessage(input[0]))