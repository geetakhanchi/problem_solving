#WAF take a integer x as input,print all the odd valves from 1 to x
def my_function(a):
    b = 0
    while b <= a:
        b += 1
        if b % 2 == 1:
            print(b)

my_function(7)
