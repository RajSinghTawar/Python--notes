# exception handling
# try exept else finally
 
while True:
    try:
        age = int(input('enter your age: ')) # seven # 7
        break
    except ValueError:
        print('maybe you entered string instead of number , try again')
    except:
        print('unexcepted error ....')

if age < 18:
    print('You can\'t play this game.')
else:
    print('You can play this game.') 