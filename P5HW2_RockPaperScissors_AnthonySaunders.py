# Create a Rock, Paper, Scissors Game
#11-5-2018
#CTI-110 P5HW2 Rock,Paper,Scissors
#Anthony Saunders

#import random
import random


# Define raw input
raw_input = input
# Define the computer choice function
def rps():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()



# Define Function when computer chooses Rock
def computer_choice_rock():
    user_choice = raw_input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print("You Tie. You chose Rock and the computer chose Rock.")
        try_again()
    if user_choice == "2":
        print("You Win. You chose Paper and the computer chose Rock.")
        try_again()
    if user_choice == "3":
        print("You Lose. You chose Scisors and the computer chose Rock.")
        try_again()
    else:
        print("Try again")
        computer_choice_rock()


# Define Function when computer chooses Paper

def computer_choice_paper():
    user_choice = raw_input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print("You Lose. You chose Rock and the computer chose paper.")
        try_again()
    if user_choice == "2":
        print("You Tie. You chose Paper and the computer chose paper.")
        try_again()
    if user_choice == "3":
        print("You Win. You chose Scisors and the computer chose paper.")
        try_again()
    else:
        print("Try again")
        computer_choice_paper()

# Define Function when computer chooses Scissors

def computer_choice_scissors():
    user_choice = raw_input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print("You Win. You chose Rock and the computer chose scissors.")
        try_again()
    if user_choice == "2":
        print("You Lose. You chose Paper and the computer chose scissors.")
        try_again()
    if user_choice == "3":
        print("You Tie. You chose Scisors and the computer chose scissors.")
        try_again()
    else:
        print("Try again")
        computer_choice_scissors()

# Define Try again function

def try_again():
    choice = raw_input("Would you like to play again? y/n ")
    if choice == "y" or choice == "yes" or choice == "Y":
        rps()
    elif choice == "n":
        print("Thank you for playing")
        quit()
    else:
        print("Try again")
        try_again()


rps()
                    
        
