#CTI -110
#P3LAB - Debugging
#Anthony Saunders
#October 7 2018




def main():
    
    #This program takes a number grade and outputs a letter grade.

    #System uses 10-point grading scale
    
    # Ask user to enter score
    score = float(input("Enter grade: "))

        # Evaluate the grade
        if score >= 90:
            # Notify user of grade A
            print("Your grade is: A")
        elif score >= 80:
            # Notify user of grade B
            print("Your grade is: B ")
        elif score >= 70:
            # Notify user of grade C
            print("Your grade is: C")
        elif score >= 60:
            # Notify user of greade D
            print("Your grade is: D")
        else:
            print("Your grade is: F")

# Program start
main()
