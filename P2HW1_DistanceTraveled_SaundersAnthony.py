Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #CTI-110
>>> #P2HW1 - Distance Traveled
>>> #Anthony Saunders
>>> #2/26/2018
>>> speed = int(input('70 '))
70 
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    speed = int(input('70 '))
ValueError: invalid literal for int() with base 10: ''
>>> speed = int(input('Enter the speed. '))
Enter the speed. 70
>>> distanceAfter6 = int(input('Enter the number 6. '))
Enter the number 6. 6
>>> distanceAfter10 = int(input('Enter the number 10. '))
Enter the number 10. 10
>>> distanceAfter15 = int(input('Enter the number 15. '))
Enter the number 15. 15
>>> distance1 = speed * distanceAfter6
>>> print('the distance after 6 is ', distanceAfter6)
the distance after 6 is  6
>>> distance2 = speed * distanceAfter10
>>> distance3 = speed * distanceAfter15
>>> print('the distance after 6 hours is ', distance1)
the distance after 6 hours is  420
>>> print('the distance after 10 hours is ', distance2)
the distance after 10 hours is  700
>>> print('the distance after 15 hours is ', distance3)
the distance after 15 hours is  1050
>>> 
