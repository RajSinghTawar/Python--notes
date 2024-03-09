# def a function
# name = ['harshit', 'mohit']

# print(func(names))
# print(func(names, reverse_str =True))

# SOLUTION
def func(l, **kwargs):
    if kwargs.get('reversed_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return[name.title() for name in l]
        
name = ['harshit', 'mohit']
print(func(name,reversed_str = True))
