# define a function 
# input

# num , iterables(tuple, list)containing numbers as args

# example 
# num = [1,2,3]
# to_power(3,*num)

# output
# list ----> [1, 8, 27]

# if user didn't pass any args then give a user a messagr 'hey you didn't pass
# *args

# else 
# return list

# NOTE - USE LIST COMPREHENSION

# SOLUTION
def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "you didn't pass any args"

nums = [1,2,3,4,5,6,7,8,9,10]
print(to_power(2, *nums))