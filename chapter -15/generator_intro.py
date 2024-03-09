# generators
# generators are iterators

# iterator , iterable 
l = [1,2,3] # this is iteratoers
# for i in l:
#     print(i) 
# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))

for num in map(lambda a : a**2, l): # this is iterable
    print(num)

