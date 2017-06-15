# Sweeney
# Assignment: Average Rain Fall

# has user enter number of years
numOfYears = int(input("How many years of data do you have? "))
# defines grandTotal of rain that has fallen for the number of years
grandTotal = 0

# loop repeats for number of year
for i in range(numOfYears):
    # defines total amount of rain that has fallen for 1 year
    totalRain = 0
    # loop that repeats for number of months in a year
    for numOfMonths in range(12):
        # gets amount of rain fallen for 1 month
        rainForMonth = int(input("How many inches in month " + str(numOfMonths + 1) + " of year " + str(i + 1) + " "))
        # adds rain that has fallen for the month to the inches of rain fallen that year
        totalRain += rainForMonth
    # calculates the average rain fallen for a year
    avRain = totalRain / 12
    # prints the year and average rain fallen for it
    print("For year ", i + 1, "the average rainfall was ", avRain, "inches. ")
    # adds average total rain fallen for the year to the number of inches fallen for all years executed
    grandTotal += totalRain
# prints the total amount of rain fallen over the number of years entered
print("\nThere was", grandTotal, "inches of rain that fell for", (numOfYears * 12), "months. ")
# prints average rain fall for number years enter and calculates the average rain fall for number of years entered
print("The average rain fall for", numOfYears, "years is", (grandTotal / (numOfYears * 12)), "inches per month. ")
