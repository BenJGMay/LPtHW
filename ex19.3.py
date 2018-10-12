from sys import argv

script, cash, free = argv

# How many ways can I call my function?

# This function calculates an hourly rate based on salary and work days
def check_salary(salary, holidays):
    print(f"You get paid £{salary} per year.\n")
    print(f"And you get {holidays} days of holiday each year.\n")
    work_days = 260 - int(holidays)
    day_rate = round(int(salary) / int(work_days), 2)
    print(f"You work {work_days} days a year.\n")
    print(f"Your day rate is £{day_rate}.\n")

#1

print("1\n")

check_salary(33600, 30)

#2

print("2\n")

monies = 36500
hdays = 35
check_salary(monies, hdays)

#3

print("3\n")
check_salary(40000 - 5000, 40 - 20)

#4

print("4\n")
check_salary(monies - 500, hdays - 5)

#5

print("5\n")
check_salary(cash, free)

#6
print("6\n")
check_salary(int(input("Your salary? \n")), int(input("Your holidays? \n")))
