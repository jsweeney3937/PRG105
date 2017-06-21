# initializes assessment tax to 60%
assTax = .6
# initializes property tax to .72%
propTax = .0072


# defines function get_info
def get_info():
    # asks user how much the property value is and stores it as a float
    prop_value = float(input("What is the piece of property valued at? "))

    # calls function calc_taxes, passing the property value as its argument
    calc_taxes(prop_value)


# defines function calc_taxes, receiving property value as its parameter
def calc_taxes(property_value):
    # calculates the assessment amount
    ass_value = property_value * assTax
    # calculates teh property tax amount
    prop_tax_value = ass_value * propTax

    # prints assessment value and property tax value
    print("The assessment value of the property is: $", format(ass_value, ",.2f"))
    print("The property tax is: $", format(prop_tax_value, ",.2f"))


# calls function get_info
get_info()
