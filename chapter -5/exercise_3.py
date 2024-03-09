# define a function that take list of words as argument and
# return list with reverse of every element in that list

# example 
# ["abc" , "tuv" , "xyz"] -----> ["cba" , "vut" , "zyx"]

def reverse_list(l):
    element = []
    for i in l:
        element.append(i[::-1])
    return element 

words = ["abc" , "tuv" , "xyz"]
print(reverse_list(words))       
