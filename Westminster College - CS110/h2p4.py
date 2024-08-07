#Programmer: Manny Fomundam
#Date: January 27, 2023
#Professor: John Bonomo
#Write a program that generates a random number between
#0 and 1 and then outputs one of the following fortunes

import random
#Creates a random number and prints it between 0.0 and 1.0
x = round(random.random(), 1)
print(x)

#If statements based on the random number will print a random statement based on the random
#number
if x >= 0.1 and x <= 0.3 :
    print("Beware the Ides of March")
elif x >= 0.4 and x <= 0.5 :
    print("Watch your back")
elif x == 0.6 :
    print("Don't talk to strangers")
elif x == 0.7 :
    print("They're out to get you")
else :
    print("Have a nide day!")
