#For each game, output one integer denoting the total number of coins showing the particular face in the end of the game.
t = int(input())
i = 1
while i <= t:
    g = int(input())
    j = 1
    while j <= g:
        val,n,q =list(map(int,input().split()))
        if n % 2 == 0:
            x = n//2
        elif n % 2 == 1:
            if val == q:
                x = n //2
            else:
                x = (n+1)//2
        print(x)
        j += 1
    i += 1
