# Sweeney
# Assignment: Pennies Per Day

# gets days worked and converts it to an int
daysWorked = int(input("How many days did you work for? "))
# initializes the total amount of money made as 0 dollars
totalMade = 0

print("Days Worked\tAmount Earned For Day\tTotal Earned For Days Worked")
print("___________\t_____________________\t____________________________")

# loop that runs for how ever many days were worked
# loop sets currentDay to daysWorked, currentDay first = 0, not 1
for currentDay in range(daysWorked):
    # multiplies 2 by the exponent of currentDay, first iteration is 2^0 which equals 1
    penniesMadeThatDay = 2 ** currentDay
    # adds penniesMadeThatDay to totalMade then sets totalMade to the new value
    totalMade += penniesMadeThatDay
    # prints the current day, starts with 0 + 1, tab, pennies made for the day, tab, and the total made over the amount of days converted to dollars and cents
    print((currentDay + 1), "\t\t\t", (penniesMadeThatDay * .01), "\t\t\t\t\t", format(totalMade * .01, ',.2f'))

# prints a new line, then the total amount made for daysWorked formatted to 2 decimal places
# sep="" makes it so that no spaces are printed between strings and variables
print("\nThe total amount of money made for ", daysWorked, " days is $", format(totalMade * .01, ',.2f'), sep="")
