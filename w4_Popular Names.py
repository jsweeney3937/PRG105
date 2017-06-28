# open the files GirlNames.txt and BoyNames.txt
girl_Names = open('GirlNames.txt', 'r')
boy_Names = open('BoyNames.txt', 'r')
# create a bool variable to use as a flag
found_boy = False
found_girl = False


def main():
    # sets global variables
    global found_boy
    global found_girl

    # sets variables to name input by user
    girl_name_input = get_girls_name_from_user()
    boy_name_input = get_boys_name_from_user()
    # searches for the name entered passed as argument
    search_girl_names(girl_name_input)
    search_boy_names(boy_name_input)

    # if the searched name was not found in the file display a message
    if not found_girl:
        print(girl_name_input, 'was not found in the list.')
    if not found_boy:
        print(boy_name_input, 'was not found in the list.')


def get_girls_name_from_user():
    # get the search name from the user
    find_girl = input("What is the girl's name? ")
    return find_girl


def get_boys_name_from_user():
    # get the search name from the user
    find_boy = input("What is the boy's name? ")
    return find_boy


def search_girl_names(girl_name_input):
    global found_girl
    # read the first item in the list
    search_girls_name = girl_Names.readline()

    # read the rest of the file
    while search_girls_name != '':

        # strip the \n from the names
        search_girls_name = search_girls_name.rstrip('\n')

        # Determine if the name in the list matches the name entered
        if search_girls_name == girl_name_input:
            print(girl_name_input, 'is in the list of names.')

            # set the found_girl flag to True
            found_girl = True

        # read the next name in the file
        search_girls_name = girl_Names.readline()


def search_boy_names(boy_name_input):
    global found_boy
    # read the first name in the list
    search_boys_name = boy_Names.readline()

    # read the rest of the file
    while search_boys_name != '':

        # strip the \n from the names
        search_boys_name = search_boys_name.rstrip('\n')

        # determine if the name in the list matches the name entered
        if search_boys_name == boy_name_input:
            print(boy_name_input, 'is in the list of names.')

            # set the found_boy flag to True
            found_boy = True

        # read the next value in the file
        search_boys_name = boy_Names.readline()

# call function main
main()

# close both files
girl_Names.close()
boy_Names.close()
