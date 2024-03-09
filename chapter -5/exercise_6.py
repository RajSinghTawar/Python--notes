# function
# [1,2,3, [1,2], [3,4]]
# 2
# use to ---> type()

def sublist_conter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

mixed = [1,2,3, [3,4]]
print(sublist_conter(mixed))
           