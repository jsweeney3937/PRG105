

# defines main function
def main():
    print("This program calculates the average of 5 test scores.")
    # gets 5 test scores
    score1 = float(input("What was the first score? "))
    score2 = float(input("What was the second score? "))
    score3 = float(input("What was the third score? "))
    score4 = float(input("What was the fourth score? "))
    score5 = float(input("What was the fifth score? "))
    # sends the 5 test scores to function calc_average as its arguments
    # the return value is assigned to variable average
    average = calc_average(score1, score2, score3, score4, score5)
    # calc_average returns the average of the 5 scores, sends it to function determine_grade
    # as its argument, then returns the letter grade to variable grade
    grade = determine_grade(average)
    # prints the average letter grade
    print("Your average grade is:", grade)


# function calc_average receives 5 test scores as its parameter
def calc_average(score1, score2, score3, score4, score5):
    # calculates the average score
    av = (score1 + score2 + score3 + score4 + score5) / 5
    # prints the average score for all 5 test as a numeric value
    print("Your average score is:", av)
    # returns the average score as its value
    return av


# function determine_grade receives the average score as its parameter, determines which
# letter grade is assigned and returns that letter grade to variable grade
def determine_grade(average):
    if 90 <= average <= 100:
        letter_grade = "A"
    elif 80 <= average <= 89:
        letter_grade = "B"
    elif 70 <= average <= 79:
        letter_grade = "C"
    elif 60 <= average <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

# calls main function
main()
