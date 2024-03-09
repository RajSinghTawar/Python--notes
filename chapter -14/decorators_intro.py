# decorators - enhance the functionality of other functions
# @ use for decorator_function

def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function

@decorator_function # this is sortcut
def func1():
    print('this is function 1')

func1()

@decorator_function
def func2():
    print('this is function 2')

func2()
# func1()
# func2()

# var = decorator_function(func1)
# var()

