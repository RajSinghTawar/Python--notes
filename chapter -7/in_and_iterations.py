# in keyword and iterations in dictionary
user_info = {
    'name' : 'harshit' ,
    'age' : 24,
    'fav_movie' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

# cheak if key exist in dictionary
#if 'name' in user_info:
#    print('present')  
#else:
#    print('not present')

# cheak if value exist in dictionary
#if 24 in user_info.values():
#    print('present')
#else:
#    print('not present')        

# loops in dictionaries
#for i in user_info.values():
#    print(i)   

# values method
#user_info_values = user_info.values()
#print(user_info_values)
#print(type(user_info_values))    

# keys method
#user_info_keys = user_info.keys()
#print(user_info_keys)
#print(type(user_info_keys))    

# items method 
#user_info_items = user_info.items()
#print(user_info_items)
#print(type(user_info_items))

for i, j in user_info.items():
    print(f"key is {i} and value is {j}")
     