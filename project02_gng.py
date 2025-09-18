# Guessing the number Game using python

import random
secret_number = random.randint(1,100)
attempts = 0

# TELL THE BASIC TO COMPUTER FOR USER

print("WELCOME TO THE NUMBER GUESSING GAME!")

print("I AM thinking a Number between  1 to 100 and "
"you Guess the Number")



#LOOPS

while True : # when condition is true then loops is start to work
    Guess=int(input("Enter a Number between 1 to 100 : "))
    attempts = attempts+1

    
    if Guess<secret_number :
        print("TOO LOW! THE NUMBER IS HIGHER")

    elif Guess>secret_number :
        print("TOO HIGH! THE NUMBER IS LOWER")    

    else:
        print(f"congratulation! you Guessed the number right in {attempts} attempts")    

        break