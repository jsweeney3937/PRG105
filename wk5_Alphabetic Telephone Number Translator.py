# blank list for converted numbers to be stored in
converted_num = []


def main():
    # assigns tel_num the value returned from function get_tel_num
    tel_num = get_tel_num()
    # run function convert_tel_num with tel_num passed as argument
    convert_tel_num(tel_num)

    # loop that runs though each letter in list converted_num
    for ch in converted_num:
        # prints each letter in list converted_num
        print(ch, end="")


def get_tel_num():
    # gets users alphanumeric telephone number
    tel_numb = input("Enter a 10 character telephone number in the format XXX-XXX-XXXX ").lower()
    # returns tel_numb value
    return tel_numb


# function that converts telephone letters into numbers, with tel_num passed as its parameter
def convert_tel_num(tel_num):
    # loop that runs for each character in tel_num
    for i in tel_num:
        # checks to see if value in tel_num is a digit
        if i.isdigit():
            # if it is a digit appends its value to converted_num
            str(converted_num.append(i))
        # checks to see if value in tel_num is a character
        if i.isalpha():
            # if value in tel_num is a character assigns a numeric value to converted_num list based on what letter it is
            if i == "a":
                i = 2
                str(converted_num.append(i))
            elif i == 'b':
                i = 2
                str(converted_num.append(i))
            elif i == 'c':
                i = 2
                str(converted_num.append(i))
            elif i == 'd':
                i = 3
                str(converted_num.append(i))
            elif i == 'e':
                i = 3
                str(converted_num.append(i))
            elif i == 'f':
                i = 3
                str(converted_num.append(i))
            elif i == 'g':
                i = 4
                str(converted_num.append(i))
            elif i == 'h':
                i = 4
                str(converted_num.append(i))
            elif i == 'i':
                i = 4
                str(converted_num.append(i))
            elif i == 'j':
                i = 5
                str(converted_num.append(i))
            elif i == 'k':
                i = 5
                str(converted_num.append(i))
            elif i == 'l':
                i = 5
                str(converted_num.append(i))
            elif i == 'm':
                i = 6
                str(converted_num.append(i))
            elif i == 'n':
                i = 6
                str(converted_num.append(i))
            elif i == 'o':
                i = 6
                str(converted_num.append(i))
            elif i == 'p':
                i = 7
                str(converted_num.append(i))
            elif i == 'q':
                i = 7
                str(converted_num.append(i))
            elif i == 'r':
                i = 7
                str(converted_num.append(i))
            elif i == 's':
                i = 7
                str(converted_num.append(i))
            elif i == 't':
                i = 8
                str(converted_num.append(i))
            elif i == 'u':
                i = 8
                str(converted_num.append(i))
            elif i == 'v':
                i = 8
                str(converted_num.append(i))
            elif i == 'w':
                i = 9
                str(converted_num.append(i))
            elif i == 'x':
                i = 9
                str(converted_num.append(i))
            elif i == 'y':
                i = 9
                str(converted_num.append(i))
            elif i == 'z':
                i = 9
                str(converted_num.append(i))
        # checks to see if value of tel_num is "-" and if it is assigns/appends it to converted_num list
        if i == "-":
            i = "-"
            str(converted_num.append(i))

# runs function main
main()
