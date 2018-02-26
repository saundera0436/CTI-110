Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #CTI-110
>>> #P2HW2 - Tip Tax Total
>>> #Anthony Saunders
>>> #2/26/2018
>>> tipAmount = float(input('Enter the tip amount. '))
Enter the tip amount. .18
>>> salesTax = float(input('Enter the sales tax.'))
Enter the sales tax. .07
>>> foodCost = float(input('Enter the food cost. '))
Enter the food cost. 50.75
>>> totalCost = tipAmount * salesTax * foodCost
>>> print(' The total food cost is ', totalCost)
 The total food cost is  0.63945
>>> totalCost = (tipAmount * SalesTax)* foodCost
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    totalCost = (tipAmount * SalesTax)* foodCost
NameError: name 'SalesTax' is not defined
>>> totalCost = (tipAmount * salesTax) * foodCost
>>> print('The total food cost is ', totalCost)
The total food cost is  0.63945
>>> totalCost = (tipAmount * foodCost) + (salesTax * foodCost) + foodCost
>>> print('The total food cost is .', totalCost)
The total food cost is . 63.4375
>>> 
