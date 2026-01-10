#stone,paper,scissor game

import random
choices = ["stone","paper", "scissor"]
user_choice = input(" enter stone,paper,or scissor: ").lower()
computer_choice = random.choice(choices)
print("computer_choice: ",computer_choice)

#BASIC RULES FOR PLAYING THIS GAME

"""
STONE BEATS SCISSORS
PAPER BEATS STONE
SCISSORS BEATS PAPER

"""

if(user_choice == computer_choice):
    print("match is tie!")

elif(user_choice == "stone" and computer_choice == "scissor"):
    print("you win the match!")

elif(user_choice == "paper" and computer_choice == "stone" ):
    print("you win the match!")

elif(user_choice == "scissor" and computer_choice == "paper"):
    print("you win the match!")


print("want to play again!")
