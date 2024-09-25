from datetime import datetime

def days_between_dates(date1, date2):

    date_format = "%d-%m-%Y"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    

    delta = d2 - d1
    
    return delta.days

birthday_day_jakub  = 30
birthday_month_jakub = 6
birthday_day_zuza = 3
birthday_month_zuza = 2

date1 = input("Enter the first date (DD-MM-YYYY): ")
date2 = input("Enter the second date (DD-MM-YYYY): ")

days_difference = days_between_dates(date1, date2)

d2 = datetime.strptime(date2, "%d-%m-%Y")
if d2.day == birthday_day_jakub and d2.month == birthday_month_jakub:
    print("Today is Jakub birthday! Happy Birthday!")
    print(f"The number of days between {date1} and {date2} is {days_difference} days.")
elif d2.day == birthday_day_zuza and d2.month == birthday_month_zuza:
    print("Today is Jakub birthday! Happy Birthday!")
    print(f"The number of days between {date1} and {date2} is {days_difference} days.")
    days_difference = days_between_dates(date1, date2)
    print(f"The number of days between {date1} and {date2} is {days_difference} days.")