# CTI - 110
# P3HW1 - Roman Numerals 
# Anthony Saunders
# 10/7/2018

# take user input as variable
# determine if variable is less than 10 and greater than 1
# if number is within the range, display roman numeral
# if number is greater than 10 or less than 1 display error

def main():
    print("Roman numeral translator for 1-10")
    invalidInput = 1
    while invalidInput == 1:
        numeralInput = int(input("Please enter a number:"))
        if numeralInput == 1:
            print("1 is I")
            invalidInput = 0
        elif numeralInput == 2:
            print("2 is II")
            invalidInput = 0
        elif numeralInput == 3:
            print("3 is III")
            invalidInput = 0
        elif numeralInput == 4:
            print("4 is IV")
            invalidInput = 0
        elif numeralInput == 5:
            print("5 is V")
            invalidInput = 0
        elif numeralInput == 6:
            print("6 is VI")
            invalidInput = 0
        elif numeralInput == 7:
            print("7 is VII")
            invalidInput = 0
        elif numeralInput == 8:
            print("8 is VIII")
            invalidInput = 0
        elif numeralInput == 9:
            print("9 is IX")
            invalidInput = 0
        elif numeralInput == 10:
            print("10 is X")
            invalidInput = 0
        else:
            print("Error, please enter a number between 1 and 10")
            invalidInput = 1
main()
