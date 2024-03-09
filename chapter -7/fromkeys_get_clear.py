# fromkeys
# d = {''name' : "unknown", 'age' : 'unknown'}

# d = dict.fromkeys(['name', 'age','height'],'unknown')
# d = dict.fromkeys(('name', 'age','height'),'unknown')
# d = dict.fromkeys('abc','unknown')
# d = dict.fromkeys(range(1,11),'unknown')
# d = dict.fromkeys(['name','age'],['unknown','unknown'])  #not difine
# print(d)

# Get method (cheak element methods)
d = {'name' : 'rohit' , 'age' : 'unknown'}
#print(d['name'])

# print(d.get('names')) #better
# if None --->False,  else ----> true

#if 'name' in d:
#    print('present')
#else:
#    print('not present')

#if d.get('names'):
#    print('present')
#else:
#    print('not present')

# d ={"name" : 'rohit'}
# d.clear()
# print(d)

d1 ={"name" : 'rohit' , 'age' : 'unknown'}
# d1 = d.copy()
d1 = d
# print(d)
# print(d1.popitem())

print(d1 is d)
