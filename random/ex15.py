# Write a function takes a string if string has 'o' print "wow" else "hello"
def my_function(variable):
    vari = False
    for x in variable :
        if x == "o":
            vari = True
            break
    if vari:
        print("wow")
    else:
        print("hello")
my_function("hellohell")
