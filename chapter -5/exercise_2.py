#  define a function which will take as a argument and this function 
# will return a reverse list

# example
# [1,2,3,4] -----> [4,3,2,1]
# ["word1" , "word2"] ----> ["word2" , "word1"]

# Note you simply do this with reverse method or [::-1]
# But try to do this with the help of append and pop method

# def reverse_list(l):
#    l.reverse()
#    return l

# def reverse_list(l):
#    return l[::-1]

def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list 

numbers = [1,2,3,4]
print(reverse_list(numbers))