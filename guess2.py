import random

random_integer = random.randint(1, 10)

total_guess = 0

while True:

    total_guess += 1
    guess_number = raw_input( "Enter a number from 1 to 10: ")

    if not guess_number.isdigit():
        print "Please enter an integer"


    else:
        guess_number = int(guess_number)
        if (guess_number < 1) or (guess_number > 10):
            print "please guess in the right range (1-10)"

        elif guess_number == random_integer:
            print "You guessed the right number!!!"
            break
        elif guess_number < random_integer:
            print "You guessed too low. Try again!"
        else:
            print "You guessed too high. Try again!"
    
print "You guessed the secret number in " + str(total_guess) + " round(s)!!!!"

