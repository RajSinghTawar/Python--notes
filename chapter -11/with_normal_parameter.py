# *args with normal parameter

def multiply_nums(num, *args):
    multiply = 1
    # print(num)
    # print(args)
    for num in args:
        multiply *= num
    return multiply

print(multiply_nums(2,3,3)) 