def numOfSteps():
    fileobj = open("input.txt")
    stepList = []
    result = 0
    current = 0
    for line in fileobj:
        stepList = stepList + [int(line.split()[0])]
    while current < len(stepList):
        if stepList[current] < 3:
            stepList[current] = stepList[current] + 1
            current = current + stepList[current] - 1
        else:
            stepList[current] = stepList[current] - 1
            current = current + stepList[current] + 1
        result = result + 1
    return result