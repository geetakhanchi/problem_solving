#You want to fix a price so that the revenue you earn from the app is maximized.
#Find this maximum possible revenue.
a = int(input())
j = 1
val = []
while j <= a:
    y = int(input())
    j += 1
    val.append(y)
val.sort()
s = len(val)
x = []
for i in range(0,s):
    x.append(val[i]*(s-i))
max = x[0]
for y in x:
    if y > max:
        max = y
print(max)
