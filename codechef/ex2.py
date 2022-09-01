# given an array of integer nums and an integer target return indices of two numbers such that they add
# up to target

# nums = [3,2,1,4,5,6]
# target = 11

# for i in range (len(nums)):
#     for j in range (i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i],nums[j])
#or

# def sol(nums,target):
#     for i in range (len(nums)):
#         for j in range (i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return[i,j]

# a = [3,2,1,4,5,6]
# b = 11
# print(sol(a,b))

#Write a program to print duplicate in a list

l = ["hello", 10, 20,40,50,10,40,30,50]
d = []
for i in range (len(l)):
    for j in range (i+1, len(l)):
        if l[i] == l[j] and l[i] not in d:
            d.append(l[i])

print(d)            
