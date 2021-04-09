#For every number N, output a single line containing the single non-negative integer Z(N).
# 1st Method
def Z(N):
    count = 0
    y = N // 5
    while True:
        if y >= 5:
            count = count + y
            y = y // 5
        elif y < 5:
            count = count + y
            break
    return count
a = int(input())
i = 1
while i <= a:
    x = int(input())
    ans = Z(x)
    print(ans)
    i += 1

# Other method of finding no. of zero's in factorial
# 2nd Method
# def func(N):
#     twos = fives = 0
#     for j in range(1,N+1):
#         k = j
#         while True:
#             if j % 2 == 0:
#                 twos += 1
#                 j = j//2
#             else:
#                 break
#         while True:
#             if k % 5 == 0:
#                 fives += 1
#                 k = k//5
#             else:
#                 break
#     if twos <= fives:
#         return twos
#     else:
#         return fives

# a = int(input())
# i = 1
# while i <= a:
#     x = int(input())
#     ans = func(x)
#     print(ans)
#     i += 1

#3rd Method
# def Z(N):
#     n = 1
#     i = 1
#     while i <= N:
#         n = n * i
#         i += 1
#     return n
# a = int(input())
#j = 1
#while j <= a:
#   x =int(input())
#     y = Z(x)
#     c = 0
#     while True:
#         if y % 10 == 0:
#             c += 1
#             y = y //10
#         else:
#             break
#     j += 1
#     print(c)
