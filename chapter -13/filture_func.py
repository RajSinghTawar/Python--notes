# filture function

def is_even(a):
    return a%2 == 0

numbers = [3,4,2,1,5,6,9,8,10]

# print(tuple(filter(lambda a:a%2==0, numbers)))
evens = (filter(lambda a:a%2==0, numbers))

# for i in evens:
#     print(i)

new_evens = [i for i in numbers if i%2 == 0]
print(tuple(evens))
print(new_evens)
