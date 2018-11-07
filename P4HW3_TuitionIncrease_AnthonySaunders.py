#Calculating Tuition for the next 5 years
#10-17-2018
#CTI - 110 Tuition Increase
#Anthony Saunders

#Assign Tuition
currentTuition = 8000

#Create Header

print("Year\tTuition\n------\t-------")



for currentYear in range ( 1, 6):
    #Calculate Tuition
    currentTuition += ( 3 / 100 ) * currentTuition
    
    #Display Tuition
    print( currentYear, "\t$", format( currentTuition, ".2f"))

       

