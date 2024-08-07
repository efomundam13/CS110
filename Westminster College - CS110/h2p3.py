#Programmer: Manny Fomundam
#Date: January 27, 2023
#Teacher: John Bonomo

import math
import sys

#Asks user of sides of a, b and c
a = float(input('Enter side for a: '))
b = float(input('Enter side for b: '))
c = float(input('Enter side for c: '))

#Problem 3a
#Description - If the three input values are not valid side lengths for a
#triangle, you should print an appropriate error message and end the program

error = 'INVALID SIDE LENGTHS'
if a + b >= c and b + c >= a and c + a >= b :
    print('Valid sides')
else :
    sys.exit(error)

#Problem 3b
#Description - Use an f-string in your print statement
#to output the area rounded to the nearest thousandth.

#Calculates and prints s
s = (a+b+c)/2
print(s)
print('\n')
#Calculates and prints area from heron's formula
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'Area = {area:.3f}')
