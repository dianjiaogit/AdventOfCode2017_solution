def adjacentSquares():
    lst = [[]]
    currentList = 0
    currentDir = 1
    currentLayer = 0
    for i in range (1, 20):
        
        lst[currentList] = lst[currentList] + i