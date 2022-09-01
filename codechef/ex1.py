# sort a list in decending order

# x = [3,6,2,4,1,8,7]
# x.sort(reverse=True)
# print(x)


# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)