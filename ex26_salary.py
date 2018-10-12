# load arguments
from sys import argv

script = argv[0]
salary = int(argv[1])

#These are set and don't need user input
weeks_in_year = 52
work_days_in_week = 5
week_days_in_year = weeks_in_year * work_days_in_week

def salary_calc():
    name = input("\nHi! What's your name? ")
    print(f"\nNice to meet you {name}. This program calculates"
    "salary assumptions for you.")
    holiday_in_year = int(input("\nHow many days of holiday do you get"
    " per year? "))
    #Thus we can set:
    working_days_in_year = week_days_in_year - holiday_in_year
    day_rate = round(int(salary) / working_days_in_year, 2)
    work_hours_per_day = 7.5
    hourly_rate = round(day_rate / work_hours_per_day, 2)
    input(f"\nOk, calulating things for you {name}...Done."
    "Press <enter> for results!")
    return (holiday_in_year, working_days_in_year, day_rate,
    work_hours_per_day, hourly_rate)

def salary_output():
    print(f"\nThere are {weeks_in_year} weeks in a year, and"
    f" {work_days_in_week} working days in a week."
    f" Therefore the number of week days in a year is about {week_days_in_year}.")
    #Minus Holiday allowance
    print(f"\nFrom this we subtract holiday allowance, for a total of"
    f" {working_days_in_year} working days.")
    #Per annum salary
    print(f"\nIf the yearly salary is £{salary} we can divide that by"
    f" {working_days_in_year} working days to get a day rate of £{day_rate}")
    #Hourly rate
    print(f"\nAnd thefore an hourly rate, assuming a {work_hours_per_day} hour"
    f"working day, of £{hourly_rate}")
    print("\n")

holiday_in_year, working_days_in_year, day_rate, \
work_hours_per_day, hourly_rate = salary_calc()

salary_output()
