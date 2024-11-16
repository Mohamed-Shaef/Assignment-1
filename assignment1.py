#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2024
Program: assignment1.py 
Author: Mohamed Shaef
The python code in this file (a1_mshaef.py) is original work written by
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

    if month == 2: #february
        return 29 if leap_year(year) else 28

    elif month in [4, 6, 9, 11]: #Months with 30 days
        return 30

    elif month in [1, 3, 5, 7, 8, 10, 12]: #Months with 31 days
        return 31
    
    else:
        raise ValueError(f"Invalid Month. Month not 1-12.")

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
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...

if __name__ == "__main__":
    ...
