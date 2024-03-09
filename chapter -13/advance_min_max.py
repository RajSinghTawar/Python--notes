# advance min() and max()

# numbers = [1,2,4,5,7]
# print(min(numbers))
# print(max(numbers))

def func(items):
    return len(items)

names = ['r', 'mohit', 'jay','veru']
# print(max(names, key = func))
print(max(names, key = lambda item : len(item)))


# student = {
#     'harshit' : {'score':90, 'age' : '24'},
#     'mohit' : {'score':75, 'age' : '45'},
#     'rohit' : {'score':76, 'age' : '56'}
# }
# print(max(student, key = lambda item : student[item]['score'])
student = [
    {'name': 'rohit', 'score' : 87, 'age' : 19},
    {'name': 'mohit', 'score' : 97, 'age' : 24},
    {'name': 'tohit', 'score' : 73, 'age' : 44}
]
print(max(student, key = lambda item:item.get('score'))['name'])