# ask a user for name 
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
name = input("enter your name = ")
i = 0 
temp_var = ""
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
    