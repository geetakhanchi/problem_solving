#rewrite small numbers from input to output.
#Stop processing input after reading in the number 42.
#All numbers at input are integers of one or two digits.
while True:
    x = input()
    a = int(x)
    if a == 42:
        break
    print(a)
