fileobj = open("input.txt")
dic = {}
valst = []

"""for line in fileobj:
    if len(line.split()) > 2:
        dic[line.split()[0]] = line.split()[3:]

for i in range (len(list(dic.values()))):
    valst = valst + list(dic.values())[i]
    
for k in range (len(valst)):
    if valst[k][-1] == ",":
        valst[k] = valst[k][:-1]
#valst = list(set(valst))
a = 0

for j in range (len(valst)):
    try:
        dic.pop(valst[j])
    except KeyError:
        a += 1
        pass """
        
for line in fileobj:
    if len(line.split()) > 2:
        dic[line.split()[0]] = (int(line.split()[1][1:-1]), line.split()[3:])
    else:
        dic[line.split()[0]] = (int(line.split()[1][1:-1]), False)

keylist = list(dic.keys())
        
for i in range(len(keylist)):
    lst = []
    if dic[keylist[i]][-1] != False:
        for j in range(len(dic[keylist[i]][-1])):
            if dic[keylist[i]][-1][j][-1] == ',':
                lst = lst + [dic[keylist[i]][-1][j][:-1]]
            else:
                lst = lst + [dic[keylist[i]][-1][j]]
        dic[keylist[i]] = (dic[keylist[i]][0], lst)
 
def getSum(d, k, v):
    if v[-1] == False:
       return v[0]
    else:
        total = v[0]
        for i in range (len(v[-1])):
            total = total + getSum(d, v[-1][i], d[v[-1][i]])
        return total

dic2 = {}

for k in range(len(keylist)):
    if dic[keylist[k]][-1] != False:
        if len(set(map(lambda x: getSum(dic, x, dic[x]), dic[keylist[k]][-1]))) > 1:
            for l in range(len(list(dic[keylist[k]][-1]))):
                dic2[dic[keylist[k]][-1][l]] = dic[dic[keylist[k]][-1][l]]
                
keylist2 = list(dic2.keys())
valuelist2 = []
numlist = []

for m in range(len(keylist2)):
    if dic2[keylist2[m]][-1] == False:
        valuelist2 = valuelist2 + [keylist2[m]]
        
for n in range(len(valuelist2)):
    numlist = numlist + [dic2[valuelist2[n]][0]]
    
# ans is 1853