# split method
# convent string to list

# user_info = 'Rohit,24'.split(',')
# print(user_info)
name,age = input("enter your name and age ").split(' ')
print(name)
print(age)

# join method
# convent list to string
user_info = ["harshit",'24']
print(','.join(user_info))