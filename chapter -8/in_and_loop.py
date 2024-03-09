# in keyword in sets and for loop

s = {'a','b','c'}

# in keyword to cheak if item is present or not in set
if 'a'in s:
    print('present')
else:
    print('not present')

# for loop
for item in s:
    print(item)

# set method
s1 = {1,2,3,4}
s2 = {3,4,5,6}

# union
# intersection
# |
union_set = s1 | s2
#print(union_set)
print(s1 & s2) # for intersection
