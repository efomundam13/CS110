#Programmer: Manny Fomundam
#Date: January 27, 2023
#Teacher: John Bonomo

#Problem 1a
#a = 3, b = 4, c = 5
#if b > 0 or a > c and a > b :
    #print("yes")
#else :
    #print("no")
#output would be yes

#Problem 1b
#a = 3, b = 4, c = 5
#if c%a > c%b :
    #print("oui")
#else :
    #print("non")
#output would be oui

#Problem 1c
#a = 3, b = 4, c = 5
#if a < b :
    #if a > c :
        #print("si")
    #elif c > b :
        #print("tal vez")
#else :
    #print("no")
#Output would be tal vez

#Problem 1d
#a = 3, b = 4, c = 5
#if a < b :
    #d = b
#elif a < c :
    #d = c
#print(d)
#Output would be 4

#Problem 1e
#a = 3, b = 4, c = 5
#if a < b :
    #d = b
#if a < c :
    #d = c
#print(d)
#Output would be 5

#Problem 2
#Asks user to enter the password and reenter password
password_1 = input('Enter new password: ')
password_2 = input('Reenter new pasword: ')

#If-else statements to determine if passwords are the same
if password_1 == password_2 :
    print('password updated')
else :
    print('passwords do not match')


