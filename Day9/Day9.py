fileobj = open("input.txt")
a = fileobj.readline()
lst = []
i = 0
score = 1
checkStream = False
checkGarbage = False
total = 0

while i in range(len(a)):
    if a[i] == "!":
        i += 2
    lst = lst + [a[i]]
    i += 1

for j in range(len(lst)):
    if lst[j] == "{" and checkStream == False and checkGarbage == False:
        checkStream = True
        total = total + score
    elif lst[j] == "{" and checkStream == True and checkGarbage == False:
        checkStream = False
        score += 1