# any, all function
numbers1 = [2,4,6,8,10]
numbers2 = [1,3,5,7,9]

# print(all([num%2==0 for num in numbers1]))
print(any([num%2==0 for num in numbers2]))


even = []
for num in numbers1:
    even.append(num%2==0)
# print(even)
# print([True, True, True, True, True]) # ----> true
