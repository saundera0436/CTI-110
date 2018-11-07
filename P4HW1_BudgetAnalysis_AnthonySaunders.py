#Determining if you are on budget
#10-17-2018
#CTI-110 P4HW1 - Budget Analysis
#Anthony Saunders

#Ask user to enter budget for the month while assigning it to a variable

userBudget = float(input("Please enter how much you have budgeted for the month: "))

#Assign Expenses
moreExpenses = 'y'
userTotalExpenses = 0

#Comparing Budget and expenses
while moreExpenses == 'y':
    #Ask user to enter expense
    userExpense = float(input("Enter an expense: "))

    #Calculate total expenses
    userTotalExpenses = userTotalExpenses + userExpense
    
    #Ask user if there are more expenses
    moreExpenses = input("Do you have more expenses?: Type y for yes, any key for no:")

if userTotalExpenses > userBudget:
    #Display if user is over budget
    print("You were over your budget of","$",userBudget , userTotalExpenses - userBudget)

elif userBudget > userTotalExpenses:
    #Display if user is under budget
    print("You were under your budget of","$",userBudget , format(userBudget - userTotalExpenses, ".2f"))

else:
    #Display if user is on budget
    print("You used exactly your budget of","$", format(userBudget, ".2f"),".")

                                                                                       

    
                                                                                 
