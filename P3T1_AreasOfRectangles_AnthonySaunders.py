#CTI - 110
#Area of a rectangle
#Anthony Saunders
#October 7 2018

#Ask user to input the length and width of rectangle 1.
length1 = int(input("Please enter the length of rectangle 1: "))
width1 = int(input("Please enter the width of rectangle 1 : "))

#Ask user to input the length and width of rectangle 2.
length2 = int(input("Please enter the length of rectangle 2: "))
width2 = int(input("Please enter the width of rectangle 2 : "))

#Calculate the area of rectangles.
area1 = length1 * width1
area2 = length2 * width2

#Determine which area is greater

if area1 > area2:
    print ("Rectangle 1 has the greater area")
elif area2 > area1:
    print("Rectangle 2 has the greater area")
else:
    print ("Both rectangles area is the same")
