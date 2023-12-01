f = open("./inputs/day01.txt", "r")
input = f.read().splitlines()

nums = []
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def checkDigit(i, string):
    curr = i
    numstr = string[i]
    exists = True

    while exists:
        # print(numstr)
        exists = False
        if numstr in digits:
                # print("Found in checkDigit %s" % numstr)
                return str(digits.index(numstr) + 1)
        else:
            for digit in digits:
                if numstr == digit[:len(numstr)]:
                    # print("%s matches %s" % (numstr, digit))
                    curr += 1
                    if (curr >= len(string)):
                        # print("Out of bounds %d" % curr)
                        return ''
                    numstr += string[curr]
                    exists = True
                    break
        
                
    return ''

for line in input:
    first = ''
    last = ''

    print("LINE: %s" % line)
    i = 0
    while i < len(line):
        if (line[i].isnumeric()):
            first = line[i] if first == '' else first
            last = line[i] if first != '' else last
            # print("Found %s" % line[i])
            # print("FIRST: %s LAST: %s" % (first, last))
        else:
            numstr = checkDigit(i, line)
            if numstr == '':
                i += 1
                continue
            first = numstr if first == '' else first
            last = numstr if first != '' else last
            # print("Found %s" % numstr)
            # print("FIRST: %s LAST: %s" % (first, last))

        i += 1

    print("FINAL: %s %s" % (first, last))
    nums.append(int(first + (last or first)))

# print(nums)
print(sum(nums))