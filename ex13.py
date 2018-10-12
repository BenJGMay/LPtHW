# loads the argv module from the system

from sys import argv
# read the WYSS section for how to run this
# This sets each variable to an argument passed in when the script was run
script, first, second, third, fourth = argv

#prints out the variables input - added my line breaks for readability
print("\nThe script is called:", script)
print("\nYour first variable is:", first)
print("\nYour second variable is:", second)
print("\nYour third variable is:", third)
# drill - trying another syntax
print(f"\nYour fourth variabe is: {fourth}")

weekday = input("\nWhat day of the week is it? ")

print(f"\nIs that so? Ok, so it's {weekday} today!\n")
