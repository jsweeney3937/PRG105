# opens file "names.txt" and reads it
file1 = open('names.txt', 'r')
# sets count to 0
count = 0

# loop that runs for a reads every line in the file
for line in file1:
    # prints the current line it is on
    print(line)
    # adds 1 to count and sets it as new value
    count += 1
# closes file
file1.close()
# prints the number of names read in the file
print("The number of names read in the file is:", count)
