# Sweeney
# Assignment: Day of the Week

day = int(input("Enter a number 1-7 "))
if day == 1:
    print("Monday")
if day == 2:
    print("Tuesday")
if day == 3:
    print("Wednesday")
if day == 4:
    print("Thursday")
if day == 5:
    print("Friday")
if day == 6:
    print("Saturday")
if day == 7:
    print("Sunday")
if day > 7 or day < 1:
    print("Error! You have entered a number outside the range of 1-7")
