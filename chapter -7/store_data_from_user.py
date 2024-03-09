# users = {
#     'name' : 'rohit',
#     'age' : 24,
#     'fav_movie' : ['coco','avenger'],
#     'fav_songs' : ['song1','song2'],
# }
user = {}

name = input('what is your name : ')
age = input('what is your age : ')
fav_movie = input('your fav movie separated by comma : ').split(',') 
fav_songs = input('your fav songs separated by comma : ').split(',')

user['name'] = name
user['age'] = age
user['fav_movie'] = fav_movie
user['fav_songs'] = fav_songs
#print(user)

for key,value in user.items():
    print(f"{key} : {value}")