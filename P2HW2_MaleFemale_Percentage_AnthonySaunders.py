# Calculating male and female percentage
# 9-25
# CTI-110 P2HW2 - MaleFemale percentage
# Anthony Saunders


# Get the number of males.
males = int(input("Enter the number of males in class: "))

# Get the number of females.
females = int(input("Enter the number of females in class: "))

# Calculate the number of males and females in class
maleClass = males / (males + females)
femaleClass = females / (males + females)

# Display the number of males and females in class.
print ("The class percentage for boys and girls are ", maleClass, femaleClass)
