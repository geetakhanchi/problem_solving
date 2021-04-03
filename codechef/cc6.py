#For each test case, output a single line containing the number of cars which were moving at their maximum speed on the segment.
t = int(input())
for i in range(1,t+1):
    n_car = int(input())
    c = input()
    max_speed = list(map(int,c.split()))
    s = len(max_speed)
    count = 0
    curr_com = max_speed[0]
    for v in max_speed:
        if v <= curr_com:
            count += 1
            curr_com = v
    print(count)
# time taking mehod
        # for k in range(0,j):
        #     if max_speed[j] > max_speed[k]:
        #         break
        # else:
        #     count += 1
