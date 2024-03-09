# define a function that take list of strings
# list containing reverse of every string

# NOTE - USE LIST COMP. because we already did this exercise
# using normal method 

# example
 
# def reverse_strings(l):
#     return [name[::-1] for name in l]
# print(reverse_strings(['abc', 'tuv', 'xyz']))

def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list

name = ['abc', 'tuv','xyz']
print(reverse_str(name))