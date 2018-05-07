def getSpreadsheet():
    fileobj = open("input.txt")
    result = 0
    currentList = []
    for line in fileobj:
        if line != "\n": 
            for i in range (0, len(line.split())):
                currentList = currentList + [int(line.split()[i])]
            result = result + (max(currentList) - min(currentList))
        currentList = []
    return result

#########################################################
    
def evenLyDivisible():
    fileobj = open("input.txt")
    result = 0
    currentList = []
    overallList = []
    for line in fileobj:
        if line != "\n": 
            for i in range (0, len(line.split())):
                currentList = currentList + [int(line.split()[i])]
            overallList = overallList + [currentList]
        currentList = []
    print(len(overallList))
    for i in range (0, len(overallList)):
        for x in range (0, len(overallList[i])):
            a = overallList[i][x]
            for y in range (0, len(overallList[i])):
                b = overallList[i][y] / a
                #print(a , overallList[i][y], b)
                if b % 1 == 0 and b != 1:
                    print(result)
                    result = result + b
    return result