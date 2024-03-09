# create your generator with generator function
# 1.) generator function 

# 10, 1 to 10

def nums(n):
    for i in range(1,n+1):
        yield(i)
# print(nums(10))

for number in nums(10):
    print(number)

# memory ........>1 then invisibl ho k 2, then 3

        