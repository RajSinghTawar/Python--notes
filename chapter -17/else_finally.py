# else and finally clause in exception handling

while True:
    try:
        number = int(input('enter your age: ')) 
        # break
    except ValueError:
        print('please type integer !!')
    except:
        print('unexcepected error !!! ')
    else:
        print(f'user input = {number}')
        break
    finally:
        print('finally blocks .............')

    