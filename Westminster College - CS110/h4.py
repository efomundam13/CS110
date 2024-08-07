#Programmer: Manny Fomundam
#Date: February 2, 2023
#Professor: John Bonomo

#Problem 1
#Write a method base_convert(x, b)
def base_convert(x, b):
#takes the remainder of x from b
    add = x % b
    #if x is less than/equal to 1, print 1
    if x <= 1:
        return x
    else:
        #uses recursion to get base convert
        return (str(base_convert(x//b, b)).lstrip('0') + str(add))

#Problem 2
#Write a function series_stats() that prompts the user for a series of numbers until end
#is entered and then outputs the maximum value of the series, the minimum value of
#the series and the average value of the series
def series_stats():
    maximum = None
    minimum = None
    count = 0
    total = 0

    while True:
        #Enter in a series of numbers and breaks loop when end is typed
        num = input("Enter a number (Type end to stop): ")
        if num == "end":
            break
        try:
            #Convert num to an int, incremenet count, add num to total and get average
            num = int(num)
            count = count + 1
            total += int(num)
            average = total/count
        except:
            print("BAD INPUT")
            continue

        #Determines max and min of series
        if maximum is None:
           maximum = num
        elif maximum < num:
            maximum = num
        if minimum is None:
            minimum = num
        elif num < minimum:
            minimum = num

    #Prints out max, min and average
    print("Maximum is", maximum)
    print("Minimum is", minimum)
    print("Average is", average)

#Problem 3
#Write a function times_table(b) which outputs a multiplication table in base b
def times_table(b):
    print("\n\nMultiplication Table for Base", b)

    #Create rows
    for i in range(0, b, 1):
        if i == 0:
            i =+ 1
        #Create columns
        for j in range(0, b, 1):
            if j == 0:
                j += 1
            #Multiply row and col to get product
            prod = i * j
            #Prints out and formats answers
            print(base_convert(prod, b), end="\t")
        print()

#Problem 4
#Write a function gen_key() which will generate a key 
#for the substitution cipher we went over in class
import random
import string
def gen_key():
    alphabetstring = 'abcdefghijklmnopqrstuvwxyz'
    key = ''
    #Iterates 26 times through
    for i in range (26):
        #picks a random letter from the original string
        letter = random.choice(alphabetstring)
        #adds the randomly picked letter to key
        key += letter
        #takes out the letter from the original string
        alphabetstring = alphabetstring.replace(letter,'')
    print(key)

#Problem 5
#Write two methods for each of these standards – one to calculate a
#check digit and one to check for the validity of the ISBN number
def calc_check_digit10(isbn):
    #Takes out all extra spaces and dashes from string
    isbn = isbn.replace('-', '')
    isbn = isbn.replace(' ', '')
    
    total = 0
    check_digit = 0
    #If check_valid10 is false
    if(check_valid10(isbn) == False):
        #Iterates through and calculates the total
        for i in range(len(n)):
            str_index = n[i]
            num = int(str_index)
            total += (i + 1) * num
        #Calculates check_digit
        check_digit = total % 11
    #Condition if the last digit is a 10
    if check_digit == 10:
        return 'X'
    else:
        return check_digit  
   
def check_valid10(isbn):
    #Takes out all extra spaces and dashes from string
    isbn = nisbn.replace('-', '')
    isbn = nisbn.replace(' ', '')

    #If length is 10 digits
    if(len(isbn) == 10):
        #If n is all digits
        if(isbn.isdigit()):
            total = 0
            for i in range(9):
                total += int(isbn[i]) * (i +1)
            #If checkdigits match or not
            if total % 11 == int(isbn[9]):
                return True
            else:
                return False
                sys.exit("Check digits don't match")
        else:
            #If n is not all digits
            return False
            sys.exit('Must be all numbers')
    else:
        #If n is less/more than 10 digits
        return False
        sys.exit('Must have 10 digits')

def calc_check_digit13(isbn):
    #Takes out all extra spaces and dashes from string
    isbn = isbn.replace('-', '')
    isbn = isbn.replace(' ', '')

    total = 0
    check_digit = 0
    #If check_valid13 is false
    if(check_valid13(isbn) == False):
        #Iterates through each digit and calculates total
        for i in range(len(isbn)):
            str_index = isbn[i]
            num = int(str_index)
            if i % 2:
                total += num * 3
            else:
                total += num * 1
            #Calculates check_digit
        check_digit = (10 - total % 10) % 10
    return check_digit 

def  check_valid13(isbn):
    #If length is 13 digits
    if(len(isbn)==13):
        #If all are digits
        if(isbn.isdigit()):
            total = 0
            #Iterates through eachh digit and totals them up
            for i in range(13-1):
                if i % 2:
                    total += int(isbn[i]) * 3
                else:
                    total += int(n[i]) * 1
            #If check digits match or not
            if (11 % (total % 11)) == int(isbn[13-1]):
                return True
            else:
                return False
                sys.exit("Check digits don't match")
        else:
            #If isbn is not all numbers
            return False
            sys.exit('Must be all numbers')
    else:
        #If isbn is less/more than 10
        return False
        sys.exit('Must have 10 digits')
