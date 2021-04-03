#Given an Integer N, write a program to reverse it.
x = input()
a = int(x)
i = 1
while i <= a:
    y = input()
    s = len(y)
    z = y[-1:-(s+1):-1]
    k = len(z)
    c = 0
    j = 0
    while j <= k-1:
        if z[j] == '0':
            c += 1
        else:
            break
        j += 1
    for b in range(c,k):
        print(z[b],end="")

    i += 1
    print()
