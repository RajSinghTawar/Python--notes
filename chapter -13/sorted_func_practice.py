fruits = ['mango', 'grapes', 'apple']
# sort
fruits.sort()
print(fruits)

fruits2 = ('mango', 'grapes', 'apple')
print(sorted(fruits2))

fruits3 = {'mango', 'grapes', 'apple'}
print(sorted(fruits3))

guitars = [
    {'modal1': 'yamaha f310', 'price': 8400},
    {'modal1': 'faith naptune', 'price': 50000},
    {'modal1': 'faith apollo venus', 'price': 35000},
    {'modal1': 'taylor 814ce', 'price': 450000}
]
sorted_guitars = sorted(guitars, key = lambda d:d['price'], reverse = True)
print(sorted_guitars)