fileobj = open("input.txt")
registers = {}
total = []
record = []


for line in fileobj:
    total = total + [line.split()]

for i in range(len(total)):
    registers[total[i][0]] = 0
    registers[total[i][-3]] = 0
    
def condition(lst, dic):
    if lst[-2] == '>':
        if dic[lst[-3]] > int(lst[-1]):
           calculate(lst, dic)
    elif lst[-2] == '>=':
        if dic[lst[-3]] >= int(lst[-1]):
           calculate(lst, dic)
    elif lst[-2] == '==':
        if dic[lst[-3]] == int(lst[-1]):
           calculate(lst, dic)
    elif lst[-2] == '!=':
        if dic[lst[-3]] != int(lst[-1]):
           calculate(lst, dic)
    elif lst[-2] == '<=':
        if dic[lst[-3]] <= int(lst[-1]):
           calculate(lst, dic)
    elif lst[-2] == '<':
        if dic[lst[-3]] < int(lst[-1]):
           calculate(lst, dic)
            
def calculate(lst, dic):
    if lst[1] == 'inc':
        dic[lst[0]] += int(lst[2])       
    else:
        dic[lst[0]] -= int(lst[2])
        
for i in range(len(total)):
    condition(total[i], registers)
    record = record + [registers[total[i][0]]]