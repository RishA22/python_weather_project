import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    t = datetime.fromisoformat(iso_string)
    datetime_obj = t.strftime("%A %d %B %Y")

    return datetime_obj


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    celsius = (float(temp_in_farenheit) - 32.00) * float(5.00 / 9.00)
    
    return round(celsius,1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    n = len(weather_data)
    for i in range(0, len(weather_data)):
        weather_data[i] = float(weather_data[i])
    get_sum = sum(weather_data)
    mean = get_sum / n 

    return round(float(mean),5)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file, encoding="utf-8") as read_obj: 
        csv_reader = csv.reader(read_obj) 
        next(csv_reader)
        data_list = []

        for lines in csv_reader:
            if len(lines) == 0:
                continue
            date = lines[0]
            min=int(lines[1])
            max=int(lines[2])
            data_list.append([date,min,max])

    return data_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if len(weather_data)>0:
        min_value= (float(weather_data[0]), 0)
        for i, value in enumerate(weather_data):
            if float(value) <= min_value[0]:
                min_value= (float(value), i)
    else:
        min_value=()

    return min_value
    

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if len(weather_data)>0:
        max_value= (float(weather_data[0]), 0)
        for i, value in enumerate(weather_data):
            if float(value) >= max_value[0]:
                max_value= (float(value), i)
    else:
        max_value=()

    return max_value


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    date_data=[]
    min_data=[]
    max_data=[]

    for item in weather_data:
        date_data.append(convert_date(item[0]))
        mn=convert_f_to_c(item[1])
        min_data.append(mn)
        mx=convert_f_to_c(item[2])
        max_data.append(mx)

        min_mean= format_temperature(round(calculate_mean(min_data),1))
        max_mean= format_temperature(round(calculate_mean(max_data),1))

        min_temp= format_temperature(round(min(min_data),1))
        max_temp= format_temperature(round(max(max_data),1))

        min_temp_data= date_data[min_data.index(min(min_data))]
        max_temp_date=date_data[max_data.index(max(max_data))]

        summary = (f'{len(date_data)} Day Overview\n  The lowest temperature will be {min_temp}, and will occur on {min_temp_data}.\n  The highest temperature will be {max_temp}, and will occur on {max_temp_date}.\n  The average low this week is {min_mean}.\n  The average high this week is {max_mean}.\n')

    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary=""
    for item in weather_data:
            dt= convert_date(item[0])
            mn_temp=format_temperature(convert_f_to_c(item[1]))
            mx_temp= format_temperature(convert_f_to_c(item[2]))

            daily_summary += (f"---- {dt} ----\n  Minimum Temperature: {mn_temp}\n  Maximum Temperature: {mx_temp}\n\n")

    return daily_summary