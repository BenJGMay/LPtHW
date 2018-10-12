# Here's some new strange stuff, remeber type it exactlyself.

# Sets days as a string
days = "Mon Tue Wed Thu Fri Sat Sun"
# Sets months as a string using the escape n to put in line breaks
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Prints here are the days and then the days variable
print("\nHere are the days: ", days)
# As above but for months
print("\nHere are the months: \n", months)

# prints this string. 3x" seems to cause in-code line breaks to be
# treated as such when printed
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if want, or 5, or 6.
""")
