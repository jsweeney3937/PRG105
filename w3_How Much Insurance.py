# initializes the recommended insurance amount needed as a global variable
ins_percent = .8


# main function
def main():
    # gets the amount it would cost to replace the building
    building_amount = int(input("How much will it cost to replace the building? "))
    # calls the function "calc_ins_amount" and passes building_amount as its argument
    calc_ins_amount(building_amount)


# calc_ins_amount function that receives prop_amount as its parameter
def calc_ins_amount(prop_amount):
    # calculates the minimum amount of insurance needed
    ins_needed = prop_amount * ins_percent
    # prints the minimum suggested amount of insurance needed
    print("The minimum amount of insurance suggested is: $", format(ins_needed, ',.2f'), sep="")


# executes the function "main"
main()
