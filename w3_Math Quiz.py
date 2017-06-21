# imports random number module
import random


# defines function main
def main():
    # initializes again to "y"
    again = "y"
    # loop that runs as long as again is equal to "y"
    while again == "y":
        # generates a random number between 1 and 1000 and sets it to value1 and value2
        value1 = random.randint(1, 1000)
        value2 = random.randint(1, 1000)
        # adds the sums of the two random number and sets it to correct answer
        correct_answer = value1 + value2
        # asks user what the sum of the two random numbers is
        print("What is the sum of", value1, "+", value2, "? ")
        # gets users answer as an integer
        user_answer = int(input("What is the answer? "))
        # sends the correct answer and the user answer to function is_user_correct as arguments
        is_user_correct(correct_answer, user_answer)
        # ask user if they want to continue the program by reassigning a value to variable "again"
        again = input("Do you want to take another quiz? ")
    # prints user has quit the program once loop has terminated
    print("You have quit the program. ")


# defines function is_user_correct with the correct and user answers as its parameter
def is_user_correct(correct_answer, user_answer):
    # checks to see if the users answer is the correct answer
    if user_answer == correct_answer:
        # if user answer is correct answer prints congratulations
        print("Congratulations")
    else:
        # if users answer is incorrect prints the correct answer
        print("The correct answer is:", correct_answer)

# runs function "main"
main()
