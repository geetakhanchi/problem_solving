#Take a list as input ,print the sum of all valve in list
n = input()
b = list(map(int,n.split()))
s = len(b)
i = 0
a = 0
while i <= s-1:
    a = a + b[i]
    i += 1
print(a)
