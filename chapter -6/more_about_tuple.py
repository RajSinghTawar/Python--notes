# looping in tuples
# tuple with one element
# tuple without parenthises 
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1,2,3,4.0)

# for loop and tuple
for i in mixed:
    print(i)
# NOTE - you can use while loop too

# tuple with one element
nums = (1,)
word = ("word1",)
print(type(nums))    
print(type(word))    

# tuple without parenthesis
guitars = 'yamaha' , 'baton rouge' , 'taylore'
print(guitars)

# tuple unpacking 
guitarists = ('maneli jamal', 'eddie van der meerr', 'andrew foy')
guitars1 , guitars2, guitars3 = (guitarists)
print(guitars1)

# list inside tuple
favorites = ("southern magnolia", ["tocyo dhoul theme", 'landscape'])
favorites[1].append("we made it")
print(favorites)

# min and max and sum
print(max(mixed))