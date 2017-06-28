# initializes 0 as the average
av = 0
# initializes 0 as the total of all numbers in file numbers.txt
totalNum = 0
# initializes 0 as the number of numbers in file numbers.txt
count = 0


# defines function main
def main():
    # declares global variables
    global totalNum
    global count
    global av

    try:
        # opens file named numbers.txt and reads it only
        file1 = open('numbers2.txt', 'r')
        # loop that reads each value line by line
        for line in file1:
            # adds the value of each number to total of numbers and reassigns its value
            totalNum += int(line)
            # adds 1 to count
            count += 1
        # calculates the average of total value of numbers from numbers.txt and divides it by
        # count, the total number of values in numbers.txt
        av = (totalNum / count)
        # prints the total value, number of items in file, and average
        print("The total of the values in 'numbers.txt' is:", totalNum)
        print("The number of values in 'numbers.txt' is:", count)
        print("The average of the numbers in 'numbers.txt' is: ", av)
    except IOError as er:
        print(er)
    except ValueError as er:
        print(er)

# calls function main
main()
