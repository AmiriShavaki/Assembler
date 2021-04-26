def deleteComments(line):
    for i in range(len(line)):
        if line[i] == '#':
            return line[:i]
    return line

def deleteLabels(line, labelLineInd, ind):
    for i in range(len(line)):
        if line[i] == ':':
            labelLineInd[line[:i]] = ind
            return line[i + 1:]
    return line

def myPrint(l):
    for i in l:
        print(i)

def deleteComma(s):
    if s[-1] == ',':
        return s[:-1]
    return s

inFile = open("Input.asm", 'r')
outFile = open("output.txt", 'w')

inputLines = inFile.readlines()

labelLineInd = {}

for lineInd in range(len(inputLines)):
    inputLines[lineInd] = deleteLabels(deleteComments(inputLines[lineInd]), labelLineInd, lineInd)
    inputLines[lineInd] = inputLines[lineInd].split()
    for i in range(len(inputLines[lineInd])):
        inputLines[lineInd][i] = deleteComma(inputLines[lineInd][i])

myPrint(inputLines)

inFile.close()
outFile.close()
