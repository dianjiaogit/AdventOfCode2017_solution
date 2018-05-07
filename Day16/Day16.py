fileobj = open("input.txt")

lst = list(fileobj.readline().split(","))
lst[-1] = 's6'
#lst = ['s1','x3/4','pe/b','pa/b','s3','x1/4']
prog = []

for i in range(ord('a'), ord('p') + 1):
    prog = prog + [chr(i)]
    
def getFstNum(string):
    a = string.index('/')
    return int(string[1:a])

def getSndNum(string):
    a = string.index('/')
    return int(string[a + 1:])

for j in range(len(lst)):
    if lst[j][0] == 's':
        prog = prog[-int(lst[j][-1]):] + prog[:-int(lst[j][-1])]
    elif lst[j][0] == 'x':
        temp = prog[getFstNum(lst[j])]
        prog[getFstNum(lst[j])] = prog[getSndNum(lst[j])]
        prog[getSndNum(lst[j])] = temp
    elif lst[j][0] == 'p':
        a = prog.index(lst[j][1])
        b = prog.index(lst[j][-1])
        prog[b] = lst[j][1]
        prog[a] = lst[j][-1]
    print(prog)
        
#ibefnclmoagdhjkp