# ask a user for name and count each character 
# example - Harshit vashisth
# print count of each words
# output : 
# H : 1
# a : 2
# r : 1
# s : 3
# h : 3
# i : 2
# t : 2
#   : 1
# V : 1

# SOLUTION
name = input("please enter a name = ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
    temp += name[i]

    