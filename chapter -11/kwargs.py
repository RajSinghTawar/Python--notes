# kwargs (keyword argument)
# **kwargs (double star operator)

# kwargs as a parameter
def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")
# func(first_name = 'rohit', last_name = 'tanwar')

# dictionary unpacking
d = {'name' : 'rohit', 'age' : 24}
func(**d)