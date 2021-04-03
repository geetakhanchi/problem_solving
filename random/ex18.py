#Take input from user and print the sum of two integer
inp = input()
a,b = list(map(int,inp.split()))
c = a + b
print(c)

#Take a string as an input. if string is palindrome print yes else no
name = input()
s = len(name)
i = 1
x= name[-i]
while i <= s-1:
    x = x + name[-(i+1)]
    i += 1
if name == x:
    print("Yes")
else:
    print("No")
