import time
# list vs generator
# memory usage , time
# When to use list , when to use generator

# t1 = time.time()
# l = [i**2 for i in range(1000000)] # 10 million
# print(time.time() - t1)

t1 = time.time()
g = (i**2 for i in range(1000000)) # 10 million
print(time.time() - t1)