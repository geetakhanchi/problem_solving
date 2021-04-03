# sorting the given list
x = []
valves = [8,2,6,4,3]
for v in valves:
    ins = 0
    for i in range(0,len(x)):
        if x[i] > v:
            ins = i
            break
    x.insert(ins,v)
print(x)
