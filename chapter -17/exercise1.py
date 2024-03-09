# make a function 'division'
# division(a,b)

# print(division(4,2))
# print(division(4,0)) # please don't division by zero , Zero
# print(division('4',2)) # please input number only

# SOLUTION

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print ('You cannot divide a number by zero')
        print(err)
    except TypeError as err:
        print("numbers must be int or float")
    except:
        print("unexcepted error")

# print(divide(10,0))
print(divide(10,'2'))