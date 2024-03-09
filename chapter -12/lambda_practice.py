# lambda expression practice

# def even(a):
#    return a%2 == 0 # -----> true , false
# print(even(5))

is_even = lambda a : a%2 == 0
print(is_even(4))

last_char = lambda s : s[-1]
print(last_char('harshit'))

# lambda with if , else

# def func(s):
#     return len(s) > 5
# print(func('rohitt'))

func = lambda s : len(s) > 5
print(func('rohit'))