#Programmer: Manny Fomundam
#Date: January 30, 2023
#Professor: John Bonomo
#Description: prompts the user to enter a 1 if they are a single filer, a 2 if they are married,
#filing jointly, a 3 if they are married, filing separately or a 4 if they are head of household.
#prompt the user for their income and echos the input and then output the tax rate for their
#tax bracket

#Calling sys module
import sys

#Asking user ro input filing status and income
print('Please indicate your filing status: \n         1 - Filing singly \n         2 - Married, filing jointly \n         3 - Married, filing seperately \n         4 - Head of household')
status = int(input('Status --> '))
income = int(input('Please enter your yearly income --> '))

#Match statement first matches each case to the status entered by the user
#Then goe sthrough if-else statements for income entered by user to determine taxRate
match status:
    #Case for Filing singly
    case 1:
        print('\n')
        print('Status: ' + str(status))
        print('Income: $' + str(income))
        #If - else statements to determine taxRate for filing singly
        if income > 0 and income <= 10275:
            taxRate = 10
        elif income >= 10276 and income <= 41755:
            taxRate = 12
        elif income >= 41776 and income <= 89075:
            taxRate = 22
        elif income >= 89076 and income <=170050:
            taxRate = 24
        elif income >= 170051 and income <= 215950:
            taxRate = 32
        elif income >= 215951 and income <= 539900:
            taxRate = 35
        elif income >= 539901:
            taxRate = 37
        else:
            #If income is negative or zero, there cannot be a taxRate, it would be zero
            #Program would print out error message and kill the program
            sys.exit("INVALID INCOME, CAN'T CREATE A TAXRATE, PLEASE TRY AGAIN")
    case 2:
        #Case for Married, filing jointly
        print('\n')
        print('Status: ' + str(status))
        print('Income: $' + str(income))
        #If - else statements to determine taxRate for Married, filing jointly 
        if income > 0 and income <= 20550:
            taxRate = 10
        elif income >= 20551 and income <= 83550:
            taxRate = 12
        elif income >= 83551 and income <= 178150:
            taxRate = 22
        elif income >= 178151 and income <= 340100:
            taxRate = 24
        elif income >= 340101 and income <= 431900:
            taxRate = 32
        elif income >= 431901 and income <= 647850:
            taxRate = 35
        elif income >= 647851:
            taxRate = 37
        else:
            #If income is negative or zero, there cannot be a taxRate, it would be zero
            #Program would print out error message and kill the program
            sys.exit("INVALID INCOME, CAN'T CREATE A TAXRATE, PLEASE TRY AGAIN")
    case 3:
        #Case for Married, filing seperately 
        print('\n')
        print('Status: ' + str(status))
        print('Income: $' + str(income))
        if income >= 0 and income <= 10275:
            taxRate = 10
        elif income >= 10276 and income <= 41775:
            taxRate = 12
        elif income >= 41776 and income <= 89075:
            taxRate = 22
        elif income >= 89076 and income <= 170050:
            taxRate = 24
        elif income >= 170051 and income <= 215950:
            taxRate = 32
        elif income >= 215951 and income <= 325925:
            taxRate = 35
        elif income >= 325926:
            taxRate = 37
        else:
            #If income is negative or zero, there cannot be a taxRate, it would be zero
            #Program would print out error message and kill the program
            sys.exit("INVALID INCOME, CAN'T CREATE A TAXRATE, PLEASE TRY AGAIN")
    case 4:
        #Case for Head of household 
        print('\n')
        print('Status: ' + str(status))
        print('Income: $' + str(income))
        #If - else statements to determine taxRate for Head of household
        if income > 0 and income <= 14650:
            taxRate = 10
        elif income >= 14651 and income <= 55900:
            taxRate = 12
        elif income >= 55901 and income <= 89050:
            taxRate = 22
        elif income >= 89051 and income <= 170050:
            taxRate = 24
        elif income >= 170051 and income <= 215950:
            taxRate = 32
        elif income >= 215951 and income <= 539900:
            taxRate = 35
        elif income >= 539901:
            taxRate = 37
        else:
            #If income is negative or zero, there cannot be a taxRate, it would be zero
            #Program would print out error message and kill the program
            sys.exit("INVALID INCOME, CAN'T CREATE A TAXRATE, PLEASE TRY AGAIN")
    case other:
        #If status doesn't exist, then tehres not status to do taxRate under
        #Program would print out error message and kill the program
        sys.exit('INVALID STATUS, PLEASE TRY AGAIN')
    
print('Tax Rate: ' + str(taxRate) + '%')
