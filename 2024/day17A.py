from utils import getInput

inputs = getInput(17)
inputs = [x.split() for x in inputs]

A = int(inputs[0][-1])
B = int(inputs[1][-1])
C = int(inputs[2][-1])

program = list(map(int, inputs[-1][-1].split(',')))
out = []
pc = 0

def get_combo(operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C

while pc < len(program):
    match program[pc]:
        case 0:
            n = A
            operand = program[pc+1]
            d = 2 ** get_combo(operand)
            A = n // d
            pc += 2

        case 1:
            operand = program[pc+1]
            B ^= operand
            pc += 2
        
        case 2:
            B = get_combo(program[pc+1]) % 8
            pc += 2
        
        case 3:
            if A == 0:
                pc += 2
            else:
                pc = program[pc+1]
        
        case 4:
            B ^= C
            pc += 2
        
        case 5:
            out.append(get_combo(program[pc+1]) % 8)
            pc += 2
        
        case 6:
            n = A
            operand = program[pc+1]
            d = 2 ** get_combo(operand)
            B = n // d
            pc += 2 

        case 7:
            n = A
            operand = program[pc+1]
            d = 2 ** get_combo(operand)
            C = n // d
            pc += 2

print(",".join(map(str, out)))
