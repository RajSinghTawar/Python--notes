def greater(a,b):
    if a>b:
        return a
    else:
        return b

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else: 
        return c

def new_greater(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c) 
    # return greater(geater(a,b), c) {it also cab be write}
print(new_greater(100,19,15))    

# functio inside function
# greater(a,b)------> a or b
# greatest(a,b,c)------->greatest