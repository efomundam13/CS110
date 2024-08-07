#Programmer: Manny Fomundam
#Date: January 19, 2023
#Professor: John Bonomo
#Description: Write a program that asks the user how many of each type of
#ticket they they want and then outputs how many total tickets they asked
#for and the total cost

#Create variable for cost of each ticket
children_Ticket_Price = 5.00
adult_Ticket_Price = 8.00
senior_Ticket_Price = 6.00

#Asks user for the amount of tickets for children, adults and seniors
children_Ticket_Number = float(input('Number of children tickets: '))
adult_Ticket_Number = float(input('Number of adult tickets: '))
senior_Ticket_Number = float(input('Number of senior tickets: '))
print('\n')

#Multiplies the price of tickets to the number of them to get tickey
#totals for children, adults and seniors
children_total = float(children_Ticket_Price * children_Ticket_Number)
adult_total = float(adult_Ticket_Price * adult_Ticket_Number)
senior_total = float(senior_Ticket_Price * senior_Ticket_Number)

#Prints out total costs for tickets for children, adults and seniors seperately
print("Children total = " + str(children_total))
print("Adult total = " + str(adult_total))
print("Senior total = " + str(senior_total))
print('\n')

#Prints out total number of tickets and total costs of all tickets
totalTickets = float(children_Ticket_Number + adult_Ticket_Number + senior_Ticket_Number)
print("Total Amount of Tickets: " + str(totalTickets) + " tickets")
print('\n')
totalCost = float(children_total + adult_total + senior_total)
print("Total Cost: $" + str(totalCost))

