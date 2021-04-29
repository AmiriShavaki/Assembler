import numpy

typeFormat = {"add": 'R', "addu": 'R', "addi": 'I',
              "and": 'R', "andi": 'I', "nor": 'R',
              "or": 'R', "ori": 'I', "sll": 'R',
              "sra": 'R', "xor": 'R', "xori": 'I',
              "slt": 'R', "sltu": 'R', "slti": 'I',
              "beq": 'I', "bne": 'I', "j": 'J', "jal": 'J',
              "lb": 'I', 'lbu': 'I', 'lw': 'I', 'lui': 'I',
              "sb": 'I', 'sw': 'I'}
funct = {"add": '100000', "addu": '100001',
         'and': '100100', 'nor': '100111', 'or': '100101',
         'sll': '000000', 'sra': '000011', 'xor': '100110',
         'slt': '101010', 'sltu': '101011'}
regNums = {'$zero': 0, '$0': 0, '$at': 1, '$v0': 2,
           '$v1': 3, '$a0': 4, '$a1': 5, '$a2': 6,
           '$a3': 7, '$t0': 8, '$t1': 9, '$t2': 10,
           '$t3': 11, '$t4': 12, '$t5': 13, '$t6': 14,
           '$t7': 15, '$t8': 24, '$t9': 25, '$s0': 16,
           '$s1': 17, '$s2': 18, '$s3': 19, '$s4': 20,
           '$s5': 21, '$s6': 22, '$s7': 23, '$k0': 26,
           '$k1': 27, '$gp': 28, '$sp': 29, '$fp': 30,
           '$ra': 31}

def convertToBin(n, k):
    return numpy.binary_repr(n, width = k)

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
machineCode = []

labelLineInd = {}

for lineInd in range(len(inputLines)):
    inputLines[lineInd] = deleteLabels(deleteComments(inputLines[lineInd]), labelLineInd, lineInd)
    inputLines[lineInd] = inputLines[lineInd].split()
    for i in range(len(inputLines[lineInd])):
        inputLines[lineInd][i] = deleteComma(inputLines[lineInd][i])
    curMachineCode = ""
    if not len(inputLines[lineInd]):
        continue
    instName = inputLines[lineInd][0]
    if typeFormat[instName] == 'R':
        curMachineCode += "0" * 6 #opcode
        if instName == 'sll' or instName == 'sra':
            curMachineCode += "0" * 5 #rs
            curMachineCode += convertToBin(regNums[inputLines[lineInd][2]], 5) #rt
            curMachineCode += convertToBin(regNums[inputLines[lineInd][1]], 5) #rd
            curMachineCode += convertToBin(int(inputLines[lineInd][3]), 5) #shamt
        else:
            curMachineCode += convertToBin(regNums[inputLines[lineInd][2]], 5) #rs
            curMachineCode += convertToBin(regNums[inputLines[lineInd][3]], 5) #rt
            curMachineCode += convertToBin(regNums[inputLines[lineInd][1]], 5) #rd
            curMachineCode += "0" * 5 #shamt
        curMachineCode += funct[instName] #funct
    elif typeFormat[instName] == 'I':
        a = 2*2
    elif typeFormat[instName] == 'J':
        a = 2*2
    print(inputLines[lineInd], curMachineCode)

myPrint(inputLines)

inFile.close()
outFile.close()
