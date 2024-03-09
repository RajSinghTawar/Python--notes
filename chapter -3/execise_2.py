# exercise - WATCH COCO
# ask user's name and age 
# if user's name start with ('a' or 'A')
# print 'you can ch coco movie'
# Else print 'sorry, you cannnot watch coco'

# SOLUTION 
user_name = input("enter your name = ")
user_age = input("enter your age = ")
user_age = int(user_age)
if user_age >= 10 and (user_name[0]=='a' or user_name[0] == 'A'):
    print("you can watch coco movie")
else:
    print("you cannot watch coco movie")    