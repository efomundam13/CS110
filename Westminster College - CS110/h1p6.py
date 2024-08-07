#Programmer: Manny Fomundam
#Date: January 20, 2023
#Professor: John Bonomo
#Description: Write a program that asks the user for three sides of a triangle
#and outputs the area of the triangle using Heron’s formula.

import math

#Asks user of sides of a, b and c
a = int(input('Enter side for a: '))
b = int(input('Enter side for b: '))
c = int(input('Enter side for c: '))

#Calculates and prints s
s = (a+b+c)/2
print(s)
print('\n')
#Calculates and prints area from heron's formula
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area = " + str(area))


