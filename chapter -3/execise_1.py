# EXECISE , NUMBER GUEDDING GAME 
# Make a variable, like winning_number and assign any number to it.
#  Ask user to guess a number .
# if user guessed correctly then print "you win !!!!"
# if user didn'd guessed correctally then :
    # if user guessed lower than actual number then print "too low".
    #  if user guessed higher than actual number then print "two high"
     
# SOLUTION
winning_number =27
user_input = input("guess a number b/t 1 and 100 = ")
user_input = int(user_input)
if user_input==winning_number:
    print("YOU WIN!!!!!")
else:
    if user_input < winning_number: 
        print("too low") 
    else:
        print("too high")           