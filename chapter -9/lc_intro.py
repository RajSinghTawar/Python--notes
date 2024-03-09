# list comprahension
# with the help of list comp. we can create of list in one line

# create a list of square from 1 to 10
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)

# square2 = [i**2 for i in range(1,11)]
# print(square2)

# nagative = []
# for i in range(1,11):
#     nagative.append(-i)
# print(nagative)

# new_negative = [-i for i in range(1,11)]
# print(new_negative)

names = ['Harshit', 'Mohit', 'Rohit']
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)

new_list2 = [name[0] for name in names]
print(new_list2)


