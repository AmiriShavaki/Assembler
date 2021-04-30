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
opCode = {'addi': '001000', 'andi': '001100', 'ori': '001101',
          'xori': '001110', 'slti': '001010', 'beq': '000100',
          'bne': '000101', 'lb': '100000', 'lbu': '100100',
          'lw': '100011', 'lui': '001111', 'sb': '101000',
          'sw': '101011', 'j': '000010', 'jal': '000011'}

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

def deleteComma(s):
    if s[-1] == ',':
        return s[:-1]
    return s

inFile = open("test.asm", 'r')
outFile = open("test.txt", 'w')

inputLines = inFile.readlines()
machineCode = []

labelLineInd = {}

for lineInd in range(len(inputLines)):
    inputLines[lineInd] = deleteLabels(deleteComments(inputLines[lineInd]), labelLineInd, lineInd)
    inputLines[lineInd] = inputLines[lineInd].split()
    for i in range(len(inputLines[lineInd])):
        inputLines[lineInd][i] = deleteComma(inputLines[lineInd][i])

for lineInd in range(len(inputLines)):
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
        curMachineCode += opCode[instName] #opcode
        if instName == "lui":
            curMachineCode += '0' * 5 #rs
            curMachineCode += convertToBin(regNums[inputLines[lineInd][1]], 5) #rt
            curMachineCode += convertToBin(regNums[inputLines[lineInd][2]], 16) #immediate
        elif instName in ['lb', 'lw', 'sw', 'sb', 'lbu']:
            im_rs = inputLines[lineInd][2].split('(')
            rs = im_rs[1][:-1]
            im = im_rs[0]
            curMachineCode += convertToBin(regNums[rs], 5)
            curMachineCode += convertToBin(regNums[inputLines[lineInd][1]], 5) #rt
            curMachineCode += convertToBin(int(im), 16) #immediate
        elif instName in ['beq', 'bne']:
            curMachineCode += convertToBin(regNums[inputLines[lineInd][1]], 5) #rs
            curMachineCode += convertToBin(regNums[inputLines[lineInd][2]], 5) #rt
            curMachineCode += convertToBin(labelLineInd[inputLines[lineInd][3]] - lineInd - 1, 16) #immediate
        else:
            curMachineCode += convertToBin(regNums[inputLines[lineInd][2]], 5) #rt
            curMachineCode += convertToBin(regNums[inputLines[lineInd][1]], 5) #rs
            if inputLines[lineInd][3] in ['$0', '$zero']:
                inputLines[lineInd][3] = 0
            curMachineCode += convertToBin(int(inputLines[lineInd][3]), 16) #immediate
            
    elif typeFormat[instName] == 'J':
        curMachineCode += opCode[instName] #opcode
        curMachineCode += convertToBin(labelLineInd[inputLines[lineInd][1]] * 4, 26)
        
    outFile.write(curMachineCode + '\n')

inFile.close()
outFile.close()
