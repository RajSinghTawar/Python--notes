name,char = input("enter comma seperate name and character = ").split(",")
print(f"lenght your name is ={len(name)}")
print(f"character count = {name.lower().count(char.lower())}")