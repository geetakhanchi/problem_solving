# Take an integer as input after that take a list as input then check the list contain that integer
c = input()
a = int(c)
x = input()
b = list(map(int,x.split()))
vari = False
for k in b:
    if a == k:
        vari = True
        break
if vari:
    print("yes")
else:
    print("No")
