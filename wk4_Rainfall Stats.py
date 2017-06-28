# initializes total_rainfall, months, monthly_rainfall (as a list with 1 content
# repeated 12 times) and month
total_rainfall = 0
months = 12
monthly_rainfall = [0] * months
month = 0


def main():
    # assigns var t_rainfall to value returned from function get_monthly_rain
    t_rainfall = get_monthly_rain()
    # assigns var average_rainfall to value returned from function calc_av,
    # t_rainfall is passed as an argument to function cal_av
    average_rainfall = calc_av(t_rainfall)
    # assigns var minimum_rain_value to value returned from function find_minimum_rainfall_value
    minimum_rain_value = find_minimum_rainfall_value()
    # assigns var minimum_rain_months to value returned from function find_minimum_rainfall_months
    minimum_rain_months = find_minimum_rainfall_months()
    # assigns var maximum_rain_value to value returned from function find_maximum_rainfall_value
    maximum_rain_value = find_maximum_rainfall_value()
    # assigns var maximum_rain_months to value returned from function find_maximum_rainfall_months
    maximum_rain_months = find_maximum_rainfall_months()
    # prints total rain fall for the year, av rain fall for each month
    # minimum amount of rain that fell and on what month
    # maximum amount of rain that fell and on what month
    print("The total rainfall for the year is:", t_rainfall)
    print("The average rainfall for each month is:", average_rainfall)
    print("The minimum amount of rain fall for the year was:", minimum_rain_value)
    print("The minimum amount of rain fall fell on month(s):", minimum_rain_months)
    print("The maximum amount of rain fall for the year was:", maximum_rain_value)
    print("The maximum amount of rain fall fell on month(s):", maximum_rain_months)


def get_monthly_rain():
    global month
    global total_rainfall
    global months
    # loop that runs as 12 times, 0-11
    while month < months:
        # gets from user how much rain fell for month "month", starting at 0
        monthly_rainfall[month] = float(input("What was the rainfall for month " + str(month + 1) + "? "))
        # adds how much rain fell that month to total_rainfall, then reassigns total_rainfall to new value
        total_rainfall += monthly_rainfall[month]
        month += 1
        # returns total_rainfall as value once counter month equals 12
        if month == 12:
            return total_rainfall


def calc_av(tot_rainfall):
    # divides tot_rainfall by 12 to get the average for each month
    av_rainfall = tot_rainfall / 12
    return av_rainfall


def find_minimum_rainfall_months():
    # creates a blank list called min_list
    min_list = []
    # sets count to 0
    count = 0
    # loop that runs 12 times
    while count < 12:
        # sees if the rainfall for month count is the minimum in list monthly_rainfall
        if monthly_rainfall[count] == min(monthly_rainfall):
                # if rainfall is minimum amount of rain fall appends its value to min_list
                min_list.append(count + 1)
        count += 1
    return min_list


def find_minimum_rainfall_value():
    # returns minimum amount of rain fall from list monthly_rainfall
    return min(monthly_rainfall)


def find_maximum_rainfall_months():
    # creates a blank list called max_list
    max_list = []
    # sets count to 0
    count = 0
    # loop that runs 12 times
    while count < 12:
        # sees if the rainfall for month count is the maximum in list monthly_rainfall
        if monthly_rainfall[count] == max(monthly_rainfall):
            # if rainfall is minimum amount of rain fall appends its value to min_list
            max_list.append(count + 1)
        count += 1
    return max_list


def find_maximum_rainfall_value():
    # finds the maximum value in list monthly_rainfall
    return max(monthly_rainfall)

main()
