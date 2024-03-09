# add and delete data
user_info = {
    'name' : 'harshit' ,
    'age' : 24,
    'fav_movie' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

# how to add data
#user_info['fav_sangs'] = ['song1','song2']
#print(user_info)

# pop mathod
#popped_item = user_info.pop('age')
#print(type(popped_item))
#print(user_info)

# popitem method
popped_item = user_info.popitem()
print(type(popped_item))
print(user_info)
