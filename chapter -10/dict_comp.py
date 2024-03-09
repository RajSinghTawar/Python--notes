# dictionary comp.
# square = {1:1, 2:4, 3:9}

# square = {num:num**2 for num in range(1,11)}
# print(square)

square = {f"square of {num} is":num**2 for num in range(1,11)}
print(square)
for i,j in square.items():
    print(f"{i}:{j}")

string = "Harshit"
# for i in string:
#     print(i)

word_count = {char:string.count(char) for char in string}
print(word_count)