#These are set and don't need user input

weeks_in_year = 52
work_days_in_week = 5
week_days_in_year = weeks_in_year * work_days_in_week
working_days_in_year = week_days_in_year - holiday_in_year
day_rate = round(salary / working_days_in_year, 2)
work_hours_per_day = 7.5
hourly_rate = round(day_rate / work_hours_per_day, 2)

print("\nThis calculates salary assumptions")

print("\nWhat is your yearly salary in £?")
# Records input as user's salary, as an interger rather than text string
salary = int(input())

print("\nHow many days of holiday do you get per year?")
# Records input as the number of holiday days the user gets
holiday_in_year = int(input())


#Work days in a year
print(f"\nThere are {weeks_in_year} weeks in a year, and {work_days_in_week} working days in a week. Therefore the number of week days in a year is about {week_days_in_year}.")
#Minus Holiday allowance
print(f"\nFrom this we subtract holiday allowance, for a total of {working_days_in_year} working days.")
#Per annum salary
print(f"\nIf the yearly salary is £{salary} we can divide that by {working_days_in_year} working days to get a day rate of £{day_rate}")
#Hourly rate
print(f"\nAnd thefore an hourly rate, assuming a {work_hours_per_day} hour working day, of £{hourly_rate}")
print("\n")
