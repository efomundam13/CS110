#Programmer: Manny Fomundam
#Date: February 24, 2023
#Professor: John Bonomo

                                                            #Written Portion
#Problem 1
#Assume we have the list fib = [1,1,2,3,5,8,13,21]. Determine what the
#following expressions return or indicate that they cause an error.
#a) fib[8]
    #Error (Index 8 does not exist)
# b) fib[-8] 
    #1
# c) fib[2:5]
    #[2,3,5]
# d) fib[3:12]
    #[3,5,8,13,21]
# e) fib[:-4]
    #5
# f) fib[-6:6]
    #[2,3,5,8]
# g) fib[2:]+fib[:2]
    #[2, 3, 5, 8, 13, 21, 2, 3, 5, 8, 13, 21]
# h) fib[5]*6
    #48
# i) fib[4:5]*6
    #[5, 5, 5, 5, 5, 5]
# j) fib + [fib.count(1)]
    #[1, 1, 2, 3, 5, 8, 13, 21, 2]


#Problem 2
#Determine what the output would be for each of the
#following lines of code, or indicate that an error occurs. or
#each set of code you should assume a starts with the value
#[’the’, ’girl’, ’hit’, ’the’, ’ball’]
# a) ball
# b) Error
# c) None
# d) 2

#Problem 3
#Write code that creates a new dictionary daysBefore which
#stores the number of days before each month
#def days_before(d):
#    month = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
#    daysBefore = {}
#    totalDays = 0
#    for month, days in d.items():
#        daysBefore[month] = totalDays
#        totalDays += days
#    return daysBefore

                                                        #Programming Portion
#Problem 4
#This is a repeat of Problem 5 in Homework 4 which asked you
#to created various functions to check for valid ISBN numbers
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

#Problem 5
#Write a function normalized(numList) that takes a list of integers numList and
#returns a new list with the normalized value of each integer
def normalized(numList):
    max_value = max(numList)
    min_value = min(numList)
    return [(num - min_value) / (max_value - min_value) for num in numList]

#Problem 6a
#Create a method sortedDictListByValue(d) which takes a dictionary
#d and returns a list of dictionary items sorted by value.
def sorted_dict_list_by_value(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

#Problem 6b
#Create a method letterFrequency(fname) which opens up a text file fname and outputs
#the number of times each letter appears in the file and the percentage of time it appears
#(it’s frequency). The letters should be output from the highest frequency to the lowest
def letter_frequency(fname):
    # Initialize a dictionary to hold the frequency of each letter
    freq_dict = {}
    # Open the file in read mode
    with open(fname, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Iterate over each character in the line
            for char in line:
                # Ignore non-alphabetic characters
                if char.isalpha():
                    # Convert the character to lowercase
                    char = char.lower()
                    # If the character is already in the dictionary, increment its count
                    if char in freq_dict:
                        freq_dict[char] += 1
                    # Otherwise, add the character to the dictionary with a count of 1
                    else:
                        freq_dict[char] = 1
    
    # Calculate the total number of letters in the file
    total_letters = sum(freq_dict.values())
    
    # Sort the frequency dictionary by value and convert it to a list of tuples
    sorted_dict_list = sorted_dict_list_by_value(freq_dict)
    
    # Iterate over each tuple in the sorted list and add its frequency
    for letter, count in sorted_dict_list:
        frequency = count / total_letters * 100
        print(f'{letter}: {count} ({frequency:.2f}%) \n')
