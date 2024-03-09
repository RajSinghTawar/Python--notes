# sum of n natural numbers
# ask a user for natural(n)
# print total from 1 to n

# SOLUTION
n = input("enter your natural number = ")
n = int(n)
total = 0
i = 1
while i<=n:
    total += i
    i += 1
    print(total)