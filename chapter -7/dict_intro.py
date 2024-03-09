# dictionaries intro
# Q - why we use dictionarie? 
# A - because of limitation of lists , lists are not enough to represent
# real data .

# Example 
#user = ['harshit', 24, ['coco','kimi no na wa'], ['awakening', 'fairy tale']]
# this list contains user name , age, fav movie, fav tunes
# you can do this but this is not a good way to do this

# Q - what are dictionaries
# A - unodered collations of data in key : value pair.

# how to create dictionaries
#user = {'name' : 'harshit', 'age' : 24}
#print(user)
#print(type(user))

# second mathod to create dictionaries 
#user1 = dict(name = 'rohit', age = 24 )
#print(user1) 

# how to access data from dictionary
# NOTE - There is no indexing because of unordered collactions of data.
#print(user["name"]) 
#print(user["age"])

# which type of data a dictionary can store ?
# anything
# numbers, strings, list , dictionary

user_info = {
    'name' : 'harshit' ,
    'age' : 24,
    'fav_movie' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}
#print(user_info['fav_movie'])

# How to add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'rohit'
user_info2['age'] = 19
print(user_info2)