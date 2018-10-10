# CTI-110 
# P3HW2 - Shipping Charges 
# Anthony Saunders
# October 7 2018
#

# ask user for weight of package
# determine which category that weight falls under
# display the shipping charges for that weight range

def main():
    print("Shipping charges by weight calculator.")
    packageWeight = float(input("Please enter the total weight of the package: "))
    if packageWeight <= 2:
           print("The cost to ship a package weighing", packageWeight,"lbs would be $1.50.")
    elif packageWeight > 2 and packageWeight <= 6:
           print("The cost to ship a package weighing", packageWeight,"lbs would be $3.00.")
    elif packageWeight > 6 and packageWeight <= 10:
           print("The cost to ship a package weighing", packageWeight,"lbs would be $4.00.")
    else:
           print("The cost to ship a package weighing", packageWeight,"lbs would be $4.75.")
main()
