print("\n")
print("This calculates salary assumptions")
#Work days in a year
print("\n")
print("There are 52 weeks in a year, and 5 working days in a week. Therefore the number of work days in a year is about", 5*52,".")
print("\n")
#Minus Holiday allowance
print("From this we subtract holiday allowance, for a total of", 52 * 5 - 30, "working days.")
print("\n")
#Per annum salary
print("If the yearly salary is £33,660.00 we can divide that by", 52 * 5 - 30, "working days to get a day rate of £", 33660.00 / (52 * 5 - 30), )
print("\n")
#Hourly rate
print("And thefore are hourly rate, assuming a 7.5 hour working day, of £", (33660.00 / (52 * 5 - 30)) / 7.5,)
print("\n")
