lst = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
lst1 = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
resultlst = []
while lst1 not in resultlst:
    maxnum = max(lst1)
    i = lst1.index(maxnum)
    lst1[i] = 0
    while maxnum > 0:
        i += 1
        if i < len(lst1):
            lst1[i] += 1
            maxnum -= 1
        else:
            i = 0
            lst1[i] += 1
            maxnum -= 1
    resultlst = resultlst + [lst]
    lst = lst1[:]

print(len(resultlst), resultlst.index(lst1))