# imports random numbers and system
import random
import sys
# defines blank lists
num_list = []
num_user = []


def main():
        # sets numbers_created to create_list
        numbers_created = create_list()
        # sets user_number to get_user
        user_number = get_user()
        # passes numbers_created and user_number as arguments to function display_num_greater...
        display_num_greater_than_users(numbers_created, user_number)


def create_list():
    # loop that runs from 0-19
    for count in range(20):
        # appeneds a random number to counts slot
        num_list.append(random.randint(1, 100))
    # returns a list size of 20, with random numbers
    return num_list


def get_user():
    global num_user
    # exception handler
    try:
        # gets a number from the user 1-100
        num_user = int(input("Enter a number between 1-100. "))
        # loop to varify number is between 1-100
        while num_user > 100 or num_user < 1:
            num_user = int(input("Enter a number between 1-100 "))
        # returns the number the user entered
        return num_user
    # handles exception to see if a letter was entered instead of a number
    except ValueError:
        # tells user they did not enter a number value
        print("You did not enter a number between 1-100. The program will exit.")
        # exits the program
        sys.exit(0)


def display_num_greater_than_users(numbers_created, user_number):
    # initializes a blank list called num_greater_than
    num_greater_than = []
    # prints the list of 20 random numbers generated and the users number entered
    print("The random numbers generated are:", numbers_created)
    print("The user number is:", user_number)
    # loop that runs for 0-19
    for count in range(20):
        # test to see if the random number is greater than the users number
        if numbers_created[count] > user_number:
            # if random number is greater than users number appends it to list num_greater_than
            # in counts slot
            num_greater_than.append(numbers_created[count])

    # checks to see if there are no numbers greater than the users number
    if not num_greater_than:
        # if no numbers greater than users number, tells user that
        print("There are no numbers greater than", user_number)
    else:
        # tells user the list of numbers that are greater than number user entered
        print("The numbers greater than the user's number are:", num_greater_than)


main()
