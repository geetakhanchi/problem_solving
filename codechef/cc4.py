# sorting of a string
x = []
ans = "ba"
for v in ans:
    ins = 0
    for i in range(0,len(x)):
        if x[i] > v:
            ins = i
            break
    else:
        ins = len(x)
    x.insert(ins,v)
print(''.join(x))
