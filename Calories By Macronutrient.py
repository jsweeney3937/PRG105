total_calories = 0


def main():
    global total_calories
    # sets grams_of_fat to user input from function get_grams_of_fat
    grams_of_fat = get_grams_of_fat()
    # sets cal_from_fat to return value of function calc_grams_of_fat, sends grams_of_fat as an argument
    cal_from_fat = calc_grams_of_fat(grams_of_fat)
    # runs function print_cal_from_fat with cal_from_fat passed as its argument
    print_cal_from_fat(cal_from_fat)
    # adds calories from fat to total calories and sets it as new value for total_calories
    total_calories += cal_from_fat

    grams_of_carbohydrate = get_grams_of_carbohydrate()
    cal_from_carbohydrate = calc_grams_of_carbohydrate(grams_of_carbohydrate)
    print_cal_from_carbohydrate(cal_from_carbohydrate)
    total_calories += cal_from_carbohydrate

    grams_of_protein = get_grams_of_protein()
    cal_from_protein = calc_grams_of_protein(grams_of_protein)
    print_cal_from_protein(cal_from_protein)
    total_calories += cal_from_protein

    print_total_calories(total_calories)


# function that gets the grams of fat consumed for the day from the user as a float and returns it
def get_grams_of_fat():
    g_of_fat = float(input("How many grams of fat did you consume today? "))
    return g_of_fat


# function calculates the calories from grams of fat, accepts user input for grams of fat
# consumed that day as an argument and returns the calculation for grams of fat to calories from fat
def calc_grams_of_fat(grams_of_fat):
    calories_from_fat = grams_of_fat * 9
    return calories_from_fat


# function that prints the calories from grams of fat, accepts the calculation from function calc_grams_of_fat
# as argument
def print_cal_from_fat(cal_from_fat):
    print("Your calories from fat are: ", cal_from_fat)


def get_grams_of_carbohydrate():
    g_of_carbohydrate = float(input("How many grams of carbohydrates did you consume today? "))
    return g_of_carbohydrate


def calc_grams_of_carbohydrate(grams_of_carbohydrate):
    calories_from_carbohydrate = grams_of_carbohydrate * 4
    return calories_from_carbohydrate


def print_cal_from_carbohydrate(cal_from_carbohydrate):
    print("Your calories from carbohydrates are: ", cal_from_carbohydrate)


def get_grams_of_protein():
    g_of_protein = float(input("How many grams of protein did you consume today? "))
    return g_of_protein


def calc_grams_of_protein(grams_of_protein):
    calories_from_protein = grams_of_protein * 4
    return calories_from_protein


def print_cal_from_protein(cal_from_protein):
    print("Your calories from protein are: ", cal_from_protein)


def print_total_calories(total_calories):
    print("Your total calories for the day are: ", total_calories)

main()
