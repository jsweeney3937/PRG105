

def get_user_input():
    # gets users name
    user_name = input("Enter your first, middle, and last name. ")
    # returns users name
    return user_name


def main():
    # sets name to what is returned from function get_user_input
    name = get_user_input()
    # splits the string dependant on spaces
    name_split = name.split()

    # loop that runs for each character in the sting
    for char in name_split:
        # prints the first char of the string as uppercase, followed by a period
        # and prints results without a new line at the end
        print(char[0].upper() + ".", end="")


main()
