# Sweeney
# Assignment: Calories Burned

# initializes number of calories burned per minute using a treadmill
calPerMinute = 4.2

# loop that executes starting at 10, ending at 31 which means it really ends at 30, and increasing start by 5 till 30 is reached
for calBurned in range(10, 31, 5):
    # prints caloires burned for whatever number of minutes calBurned is on
    print(calBurned, "minutes =", (calBurned * calPerMinute), "calories burned. ")
