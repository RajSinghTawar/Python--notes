# problem
# ask user to input a number containing more than one digit
# example  - 1256
# calculate 1+2+5+6 and print


# SOLUTION
number = input("enter a number = ")
# "1256" length=4 , last index=3
# int(number[i])


total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
    print(total)


