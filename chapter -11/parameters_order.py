# functions with all parameters 
# very important to undrstand

# PDDK

# parameters
# *args
# default parameters
# **kwargs

def func(name, *args, first_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(first_name)
    print(kwargs)
func('rohit', 1,2,3, a = 1, b = 2)
