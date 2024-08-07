#Programmer: Manny Fomundam
#Date: February 2, 2023
#Professor: John Bonomo

#Problem 1: Where v is the wind speed in miles/hr and
#t is the temperature in Fahrenheit. Write a function that
#takes v and t as arguments and returns the wind chill temperature.
def wind_chill(v, t):
    W = 35.74 + (0.6215*t) - (35.75*v**0.16) + (0.4275*t*v**0.16)
    return W

#Problem 2a
#Write a method largest3 that takes three arguments and returns the largest of them.
def largest3(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
    
#Problem 2b
#Write a method largest5 that takes five arguments and returns 
#the largest of them. This method should make use of largest3
def largest5(a,b,c,d,e):
    y = largest3(a,b,c)
    if y > d and x > e:
        return y
    elif d > y and d > e:
        return d
    else:
        return e

#Problem 3
#Write a function isLeapYear(y) which returns
#True if y is a leap year and False otherwise.
def is_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False

#Problem 4
#Write a function dayOfYear(m, d, y) which returns the
#number of days which have elapsed in year y on day m/d/y
import sys
def day_of_year(m,d,y):
    #Sets days to 0
    day = 0
    #If statements for days in each month
    if m == 1:
        if d > 31:
            sys.exit("Invalid Day for January")
        else:
            day += d
    #Specific if statements for different conditions in February
    elif m == 2:
        if(m == 2 and is_leap_year(y) and day == 29):
            day += 1
        elif(m == 2 and is_leap_year(y) == False and day  == 29):
            sys.exit("Invalid Date in February")
        elif(d > 29 and is_leap_year(y)):
            sys.exit("Invalid Day in Leap Year for February")
        elif(d > 28 and is_leap_year(y) == False):
            sys.exit("Invalid Day in a Regular Year for February")
        else:
            day += 31 + d
    elif m == 3:
        if d > 31:
            sys.exit("Invalid Day for March")
        else:
            day += 59 + d
    elif m == 4:
        if d > 30:
            sys.exit("Invalid Day for April")
        else:
            day += 92 + d
    elif m == 5:
        if d > 31:
            sys.exit("Invalid Day for May")
        else:
            day += 120 + d
    elif m == 6:
        if d > 30:
            sys.exit("Invalid Day for June")
        else:
            day +=  151 + d
    elif m == 7:
        if d > 31:
            sys.exit("Invalid Day for July")
        else:
            day += 181 + d
    elif m == 8:
        if d > 31:
            sys.exit("Invalid Day for August")
        else:
            day += 212 + d
    elif m == 9:
        if d > 30:
            sys.exit("Invalid Day for September")
        else:
            day = 243 + d
    elif m == 10:
        if d > 31:
            sys.exit("Invalid Day for October")
        else:
            day += 273 + d
    elif m == 11:
        if d > 30:
            sys.exit("Invalid Day for November")
        else:
            day += 304 + d
    elif m == 12:
        if d > 31:
            sys.exit("Invalid Day for December")
        else:
            day += 334 + d
    else:
        sys.exit("Invalid Month in a Year")

    if(m > 2 and is_leap_year(y)):
        day += 1
    else:
        day += 0
        
    return day

#Problem 5
#Write a function daysBetween(m1, d1, m2, d2, y) which returns
#the number of days between m1/d1/y and m2/d2/y.
import math
def days_between(m1, d1, m2, d2, y):
    #Calculates number of days in each date from the dayOfYear function
    date1 = dayOfYear(m1,d1,y)
    date2 = dayOfYear(m2,d2,y)

    #Subtract the diffference between teh two dates
    diff_in_dates = date1 - date2

    #returns teh absolute value of the days between the dates
    return abs(diff_in_dates)

#Problem 6
#Write a function myname() which uses turtle graphics to spell out your first or
#last name (whichever is shorter but at least 3 characters long) on the screen
import turtle
def myname():
    #Creating a turtle
    t=turtle.Turtle()
    #Letter M being drawn
    t.penup()
    t.goto(-300,50) 
    t.pendown()
    t.pensize(10)
    t.pencolor("purple")

    t.right(90)
    t.forward(150)

    t.goto(-300,50)
    t.goto(-250,-20)
    t.goto(-205,50)
    t.goto(-205,-100)

    #Letter A being drawn
    t.penup()
    t.goto(-155,50) 
    t.pendown()
    t.pensize(10)
    t.pencolor("purple")

    t.right(360)
    t.forward(150)
    
    t.goto(-155,50)
    t.right(270)
    t.forward(95)
    t.right(90)
    t.forward(150)
    t.goto(-60,-20)

    t.right(90)
    t.forward(95)

    #Letter N being drawn
    t.penup()
    t.goto(-15,50) 
    t.pendown()
    t.pensize(10)
    t.pencolor("purple")

    t.right(270)
    t.forward(150)

    t.goto(-15,50)
    t.goto(65,-90)
    t.goto(65,50)

    #Letter N being drawn
    t.penup()
    t.goto(115,50) 
    t.pendown()
    t.pensize(10)
    t.pencolor("purple")

    t.right(360)
    t.forward(150)

    t.goto(115,50)
    t.goto(195,-90)
    t.goto(195,50)
    
    #Letter Y being drawn
    t.penup()
    t.goto(245,50) 
    t.pendown()
    t.pensize(10)
    t.pencolor("purple")
    
    t.right(360)
    t.forward(100)

    t.left(90)
    t.forward(50)

    t.right(270)
    t.forward(100)

    t.right(180)
    t.forward(200)

    t.right(90)
    t.forward(500)

    turtle.done()

#Problem 7
#Write a function regular_ngon(int n) which uses turtle graphics to draw a regular
#n-sided polygon with side length 30. A regular polygon is one where all the interior
#angles are the same
import turtle
def regular_ngon(n):
    #creates a turtle
    t = turtle.Turtle()
    #for loop to run for how many sides
    for count in range(n):
        t.forward(50)
        t.left(360/n)
