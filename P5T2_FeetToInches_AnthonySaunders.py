#Converting feet to inches
#11-5-2018
#CTI-110 P5T2 Feet to inches
#Anthony Saunders



# Constant for the number of inches per foot
inches_per_foot = 12

# Main function
def main():

    # Get a number of feet from the user.
    feet = int(input("Please enter a number of feet: "))

    # Convert that to inches.
    print(feet, "feet equals", feet_to_inches(feet), "inches")

# The feet_to_inches function converts feet to inches

def feet_to_inches(feet):
    return feet * inches_per_foot

# Call the main function

main()
