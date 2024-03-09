# generate lists with range functions 
# something more about pop method
# index method
# pass list to functions
# numbers = list(range(1,11))
numbers = [1,2,3,4,5,6,7,8,9,10,]
#(numbers) 
#popped_item = numbers.pop()
#(popped_item) 
#print(numbers.index(1,3,7))

def nagative_list(l):
    nagative=[]
    for i in l:
        nagative.append(-i)
    return nagative

print(nagative_list(numbers))        