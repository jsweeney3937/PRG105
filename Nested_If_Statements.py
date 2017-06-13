# Sweeney
# Assignment: Mobile Service Provider

userPackage = input("What package do you use, package A,B, or C? ").upper()
minutesUsed = int(input("How many minutes did you use? "))
price = float

if userPackage == "A" and minutesUsed <= 450:
    price = 39.99
    print("With package", userPackage, "and ", minutesUsed, " minutes used your total comes out to $", format(price, ',.2f'))
else:
    if userPackage == "A" and minutesUsed > 450:
        price = 39.99 + ((minutesUsed % 450) * .45)
        print("With package", userPackage, "and ", minutesUsed, " minutes used your total comes out to $", format(price, ',.2f'))
    else:
        if userPackage == "B" and minutesUsed <= 900:
            price = 59.99
            print("With package", userPackage, "and ", minutesUsed, " minutes used your total comes out to $", format(price, ',.2f'))
        else:
            if userPackage == "B" and minutesUsed > 900:
                price = 59.99 + ((minutesUsed % 900) * .4)
                print("With package", userPackage, "and ", minutesUsed, " minutes used your total comes out to $", format(price, ',.2f'))
            else:
                if userPackage == "C":
                    price = 69.99
                    print("With package", userPackage, "and ", minutesUsed, " minutes used your total comes out to $", format(price, ',.2f'))
                else:
                    print("You did not enter a valid package")
