#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Fall 2024
Program: assignment1.py 
Author: Mohamed Shaef
The python code in this file (assignment1.py) is original work written by
"Mohamed Shaef". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"

    if month == 2: # february
        return 29 if leap_year(year) else 28

    elif month in [4, 6, 9, 11]: #Months with 30 days
        return 30

    elif month in [1, 3, 5, 7, 8, 10, 12]: #Months with 31 days
        return 31
    
    else:
        raise ValueError(f"Invalid Month. Month not 1-12.") #Checks for errors

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-') # Creates a string for the input from the date for year, month, and day.
    year = int(str_year) # Creates an integer for year string
    month = int(str_month) # Creates an integer for month string
    day = int(str_day) # Creates an integer for day string
    tmp_day = day + 1  # next day

 # Confirms if the day exceeds the maximum amount of days in a month
    if tmp_day > mon_max(month, year):
        to_day = 1 # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1 # Goes to the next month in line
    else:
        to_day = tmp_day # Keeps the date the same 
        tmp_month = month # Keeps the month the same

# Check if the next month is more then 12, after december the last month
    if tmp_month > 12: # If the month in greater then 12
        to_month = 1 # Move to month 1 (January)
        year += 1 # Move to the next year
    else:
        to_month = tmp_month # If it doesnt exceed December then maintain

    next_date = f"{year}-{to_month:02}-{to_day:02}" # For formatting the new date

    return next_date # Reply with the next date


def usage():
    
    "Print a usage message to the user and exit."

    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD") # demonstrates the output
    sys.exit(1)


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) # checks for leap years

def valid_date(date: str) -> bool:
    "Check validity of date and return True if valid"

    try:
        # Splits the input date into day, month, year
        str_year, str_month, str_day = date.split('-')
        year = int(str_year) # year string to integer
        month = int(str_month) # month string to integer
        day = int(str_day) # day string into integer

        if month < 1 or month > 12: # ensures that the month is not less than 1 or greater then 12
            return False
        if day < 1 or day > mon_max(month, year): # ensures that the day is not less than 1 or greater of the amount of days in the month they specified
            return False

        if len(str_year) != 4 or len(str_month) != 2 or len(str_day) != 2: # ensures that the format the user uses is correct and aligns
            return False

        return True
    except (ValueError, IndexError):
        return False




def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"

    # Starts the counter for weekend days
    weekend_days = 0
    
    if not valid_date(start_date) or not valid_date(stop_date): # Returns and error to the user if the start date or stop date they provided is incorrect
        raise ValueError("Invalid dates provided") # Returns the incorrect start or stop date error
    
    # Swaps the dates if the start date is greater than the stop provided
    if start_date > stop_date:
        start_date, stop_date = stop_date, start_date  
    
    #sets the current date as the start date
    current_date = start_date 
    
    # Checks every day in the range of start to stop
    while current_date <= stop_date:

        year, month, day = map(int, current_date.split('-')) # Checks what the year month and day of current date are 
        
        weekday = day_of_week(year, month, day) # Determines the day of the week for the current_date
        
        if weekday in ['sat', 'sun']: #Checks if its a weekend day
            weekend_days += 1 #adds to the counter of weekend days
        
        current_date = after(current_date) # Resumes to the next day
    
    return weekend_days # Returns the amount of weekend days after checking all the dates in the range

if __name__ == "__main__":

    # Checks how many arugments the user provides
    if len(sys.argv) != 3:
        usage() # Shows the user the usage method if the argument is incorrect


    start_date = sys.argv[1].strip() # The start date is first arguement
    stop_date = sys.argv[2].strip() # The stop date is the second argument

    # Checks if the start date and stop date are valid
    if not valid_date(start_date) or not valid_date(stop_date):
        usage() # If the start date and/or stop date are not valid then it shows the usage method 

    # Checks if the start date is greater then the stop date
    if start_date > stop_date:
        start_date, stop_date = stop_date, start_date # If the start date is greater than the stop date it will swap the dates


    weekends = day_count(start_date, stop_date) # the variable weekends is equal to the amount from day_count from start_date and stop_date 


    print(f"The period between {start_date} and {stop_date} includes {weekends} weekend days.") # Prints to the user the amount of weekends

