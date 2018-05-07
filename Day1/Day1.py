import sys
sys.setrecursionlimit(100000)

###################################
#Part 1

def inverseCaptcha(n):
    lst = numToList(n)
    result = 0
    for i in range (0, len(lst) - 1):
        if lst[i] == lst[i + 1]:
            result = result + lst[i]
    if lst[0] == lst[-1]:
        result = result + lst[-1]
    return result

def numToList(n):
    result = []
    if n != 0: 
        result = numToList(n // 10) + [n % 10] + result
    return result

##################################
#Part 2
    
def part2(n):
    lst = numToList(n)
    result = 0
    for i in range (0, len(lst) // 2):
        if lst[i] == lst[i + (len(lst) // 2)]:
            result = result + 2 * lst[i]
    return result