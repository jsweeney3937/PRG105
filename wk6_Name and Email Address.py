import pickle
# sets global variables
look_up = 1
add = 2
change = 3
delete = 4
QUIT = 5


# creates function main()
def main():
    # creates a blank dictionary
    email = {}
    # sets choice to 0
    choice = 0
    # sets end_of_file to false so it keeps being read
    end_of_file = False
    # opens email.dat and reads it as binary
    input_file = open('email.dat', 'rb')

    # loop that runs as long as end_of_file is false
    while not end_of_file:
        try:
            # unpickles email.dat and stores its data into email
            email = pickle.load(input_file)
        # except for end of file error
        except EOFError:
            # sets end_of_file to true and stops reading file
            end_of_file = True

    # loop that runs as long as choice does not equal quit
    while choice != QUIT:
        # sets choice to value returned from function get_menu_choice
        choice = get_menu_choice()

        # determines what route to take depending on what choice was made
        if choice == look_up:
            func_look_up(email)
        elif choice == add:
            func_add(email)
        elif choice == change:
            func_change(email)
        elif choice == delete:
            func_delete(email)
    # if users quits program, writes the elements of email into a file named email.dat
    if choice == QUIT:
        pickle.dump(email, open('email.dat', 'wb'))

        # closes input_file
        input_file.close()


# defines function get_menu_choice
def get_menu_choice():
    # prints the options to either look up, add, change, delete email or quit program
    print()
    print("Names and Emails")
    print("----------------")
    print("1: Look Up An Email")
    print("2: Add A New Email")
    print("3: Change An Email")
    print("4: Delete An Email")
    print("5: Quit The Program")
    print()

    # gets user input for choice
    choice = int(input("Enter your choice"))

    # loop that runs if choice is not a valid option, makes user enter a valid choice
    while choice < look_up or choice > QUIT:
        choice = int(input("Enter a valid choice"))

    # returns choice
    return choice


# defines function func_look_up with email passed as its parameter
def func_look_up(email):
    # gets a name to look up
    name = input("Enter a name. ")
    # gets and prints the email of the name entered, if name/key is not found prints not found
    print(email.get(name, "Not Found."))


# defines function func_add with email passed as its parameter
def func_add(email):
    # gets name to add
    name = input("Enter a name. ")
    # gets email to add
    em = input("Enter an email. ")

    # if name is not in email adds key:name and value:email
    if name not in email:
        email[name] = em
    # if name is in email prints name already exists
    else:
        print("That entry already exists. ")


# defines function func_change to change an email, var email is passed as its parameter
def func_change(email):
    # gets a name to change email address
    name = input("Enter a name. ")

    # if name is in email
    if name in email:
        # gets a new email to assign to var name
        em = input("Enter the new email")
        # assigns email key:name to new email
        email[name] = em
    else:
        print("That name is not found. ")


# defines function func_delete with email passed as its parameter
def func_delete(email):
    # gets a name to delete from dictionary email
    name = input("Enter a name. ")

    # if name is in dic email
    if name in email:
        # deletes key:name and its value from dic email
        del email[name]
    else:
        print("That name is not found. ")

# runs function main
main()
