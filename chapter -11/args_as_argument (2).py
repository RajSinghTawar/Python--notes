def multiply_nums(*args):
    multiply = 1
    # print(nums)
    # print(args)
    for num in args:
        multiply *= num
    return multiply

nums = [2,3,4]
print(multiply_nums(*nums)) # unpack chane with tuple