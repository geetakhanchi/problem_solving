# take an integer and a list as input check if list contain the two valves whose sum is equal to integer
c = input()
a = int(c)
x = input()
b = list(map(int,x.split()))
s =len(b)
vari = False
for i in range(0,s):
    for j in range(0,s):
        if i == j:
            continue
        elif b[i] + b[j] == a:
            vari = True
            break
if vari:
    print("yes")
else:
    print("No")
