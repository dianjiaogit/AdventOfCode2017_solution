#225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110
#5 = 256  6 = 257
lst = list(range(256))
currenti = 0
skip = 0
inp = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]

for i in range(len(inp)):
    if currenti + inp[i] <= 256:
        revlst = list(reversed(lst[currenti : currenti + inp[i]]))
        lst = lst[:currenti] + revlst + lst[currenti + inp[i] :]
    else:
        revlst = list(reversed(lst[currenti :] + lst[: currenti + inp[i] - 256]))
        lst = revlst[256 - currenti :] + lst[currenti + inp[i] - 256 : currenti] + revlst[: 256 - currenti]
    currenti = currenti + inp[i] + skip
    skip += 1
    if currenti >= 256:
        currenti = currenti - 256
    