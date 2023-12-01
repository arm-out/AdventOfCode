f = open("inputs/day07.txt", "r")
input = f.read().splitlines()

class Directory:
    def __init__(self, path):
        self.path = path
        self.size = -1
        self.childFiles = []
        self.childDirectories = []

class File:
    def __init__(self, path, size):
        self.path = path
        self.size = size

allDirectories = {'/': Directory('/')}
allFiles = {}
pwd = []

def createFileTree():
    # Parse commands
    for line in input:
        line = line.split(" ")
        # command
        if line[0] == '$':
            if line[1] == 'ls':
                continue
            else:
                target = line[2]
                if target =='/':
                    pwd = ['/']
                elif target == '..':
                    pwd.pop()
                else:
                    pwd += [target + '/']
        else:
            parent = allDirectories[''.join(pwd)]
            if line[0] == 'dir':
                curPath = ''.join(pwd) + line[1] + '/'
                if (curPath not in allDirectories):
                    allDirectories[curPath] = Directory(curPath)
                parent.childDirectories.append(curPath)
            else:
                curPath = ''.join(pwd) + line[1]
                if (curPath not in allFiles):
                    allFiles[curPath] = File(curPath, int(line[0]))
                parent.childFiles.append(curPath)

def dirSize(directory):
    if (directory.size >= 0):
        return directory.size
    else:
        totalFileSize = 0
        for file in directory.childFiles:
            totalFileSize += allFiles[file].size

        totalDirSize = 0
        for cDir in directory.childDirectories:
            totalDirSize += dirSize(allDirectories[cDir])
        directory.size = totalFileSize + totalDirSize
        return directory.size

createFileTree()
dirSize(allDirectories['/'])

atMostSum = 0
for dirPath in allDirectories:
    if allDirectories[dirPath].size <= 100000:
        atMostSum += allDirectories[dirPath].size

print(atMostSum)
        