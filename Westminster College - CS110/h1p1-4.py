#Name: Manny Fomundam
#Date: January 19, 2023
#Professor: John Bonomo

#Problem 1a
a = int(input('Enter number: '))
b = a + 3
c = 2 * b
d = c / 2
e = c / 2
print(a, b, c, d, e)

#Problem 1b
(e := (d := (c := (b := (a := int(input('Enter number: '))) + 3) * 2) / 2))
print(a, b, c, d, e)

#Problem 2
seconds = int(input('Enter Seconds: '))

years = seconds // 31536000
seconds = seconds - (years * 31536000)

days = seconds // 86400
seconds = seconds - (days * 86400)

hours = seconds // 3600
seconds = seconds - (hours * 3600)

minutes = seconds // 60
seconds = seconds - (minutes * 60)

seconds = int(seconds) % 60

print(str(years) + " years, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds) + " seconds")

#Problem 3a

#a = int(input('Enter a value '))
#b = int(float(a))

#It is the same for all values

#Problem 3b

#a = float(input('Enter a value '))
#b = float(int(a))

#It is not the same for all values that are not whole numbers
#Ex: if 0.1 is typed, a is equal to 0.1 while b is equal to 0.0

#Problem 4a

#Lower precendence
#3 + 2**3 = 5**3 = 125

#Higher precedence
#3 + 2**3 = 3 + 8 = 11

#Actual answer
#3 + 2**3 = 8 + 3 = 11

#Problem 4b

#left-to-right
#2**3**4 = 8**4 = 4096

#right-to-left
#2**3**4 = 2**81 = 2417851639229258349412352

#Actual answer
#2**3**4 = 2**81 = 2417851639229258349412352
