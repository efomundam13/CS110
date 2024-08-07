#Programmer: Manny Fomundam
#Date: February 13, 2023
#Professor: John Bonomo

#Problem 1
import turtle
def figure8(size):
    t = turtle.Turtle()
    for count in range(4):
        t.forward(size)
        t.left(90)
    for count in range(4):
        t.forward(size)
        t.left(270)
        

#Problem 2
def percent_raise():
    age = int(input('What is your age ---> '))
    years = int(input('How long have you been working here in years --> '))
    percentraise = 0.0

    if years < 10:
        if age < 35:
            percentraise = 1.0
        elif age < 50:
            percentraise = 1.2
        else:
            percentraise = 1.7
    elif years > 10:
        if age < 35:
            percentraise = 1.5
        elif age < 50:
            percentraise = 1.6
        else:
            percentraise = 1.7

    return "At age " + str(age) + " with " + str(years) + " of experience you may expect a raise of "  + str(percentraise) + "%"

#Problem 3
def  monthly_payments(P, n, low, high):
    t = 0
    r = low
    for count in range (low, high + 1, 1):
        r = low
        t = P(((r/100/12)*(1+(r/100/12))**(12*n))/(((1+(r/100/12))**12*n)-1))
        r += 1
        print('Interest rate ' + str(r) + '%: Monthly payment: $' + str(f't = {t:.2f}'))
        
    return 
