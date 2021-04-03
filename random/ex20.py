# Take a list as input and print the valve on odd position
name = input()
a = name.split()
s = len(a)
i = 0
while i <= s-1:
    i += 1
    if i % 2 == 1:
        x = a[i]
        print(x)
