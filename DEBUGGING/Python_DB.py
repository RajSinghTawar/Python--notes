import pdb # import pdb module
# module - python file containts useful classes functions wrote 
# by developer

# According to wikipidia - Debbuging is the process of finding and resolving 
# defects or problem within a program that prevent correct operation of computer sotware or a system.

#why debugging
# 1.) our problem is not running and cousing unexepted errors.
# 2.) our program is working fine but not working the same way we want.

# Steps for debbuging 
# 1.) set trace
# 2.) execute code line by line 

pdb.set_trace()

name = input('Please enter your name: ')
age = input('Please nter your age: ')
age2 = int(age) + 5
print(f'hello {name} you will be {age2} in next five years') 

# l (down the line)
# n (execute the code)
# c (full code run)
# q (exit)


