from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrappper(*args, **kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args, **kwargs)
        print("invalid arguments")

    #     data_types = []
    #     for arg in args:
    #         data_types.append(type(arg) == int)
    #     if all(data_types):
    #         return function(*args, **kwargs)
    #     else:
    #         print("invalid argument")
    return wrappper

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += 1
    return total

print(add_all(1,2,3,4,[1,2,3]))
