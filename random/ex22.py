# take a list as input and print how many numbers are odd and even
nam = input()
n = list(map(int,nam.split()))
count = 0
x = 0
for a in n:
    if a % 2 == 1:
        count += 1
    else:
        x +=1
print(count)
print(x)
