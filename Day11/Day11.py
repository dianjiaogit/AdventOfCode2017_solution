fileobj = open("input.txt")
lst = []

for line in fileobj:
    lst = list(line.split(','))
    
a = 0
b = 0
c = 0

for i in range(len(lst)):
    if lst[i] == 'n':
        a += 1
    elif lst[i] == 's':
        a -= 1
    elif lst[i] == 'ne':
        b += 1
    elif lst[i] == 'sw':
        b -= 1
    elif lst[i] == 'nw':
        c += 1
    else:
        c -= 1