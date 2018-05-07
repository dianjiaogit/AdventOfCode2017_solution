def validPassphrase():
    result = 0
    currentList = []
    state = False
    fileobj = open("input.txt")
    for line in fileobj:
        currentList = line.split()
        for i in range (0, len(currentList) - 1):
            for j in range (i + 1, len(currentList)):
                if currentList[i] == currentList[j]:
                    state = True
        if state == False:
            result = result + 1
        state = False
    return result

def part2():
    result = 0
    currentList = []
    state = False
    fileobj = open("input.txt")
    for line in fileobj:
        currentList = line.split()
        for i in range (0, len(currentList) - 1):
            for j in range (i + 1, len(currentList)):
                a = list(currentList[i])
                b = list(currentList[j])
                if sorted(a) == sorted(b):
                    state = True
        if state == False:
            result = result + 1
        state = False
    return result