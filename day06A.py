f = open("inputs/day06.txt", "r")
input = f.read().splitlines()

def startOfPacket(input):
    for i in range(len(input)):
        code = set([input[i], input[i+1], input[i+2], input[i+3]])
        if (len(code) == 4):
            return i+4

print(startOfPacket(input[0]))
