# Prints a question
print("\nHow old are you?", end=' ')
# Waits for a user input, which will define age
age = int(input())
# prints a question
print("\nHow tall are you?", end = ' ')
# waits for a user input, which will be height
height = input()
# prints another question
print("\nHow much do you weight?", end = ' ')
 # waits for a user input which will define weight
weight = input()
# prints a string using the above user input variables
print(f"\nSo, you're {age} old, {height} tall and {weight} heavy.")

# Here is my drill
print("\nAre you ready for another form?", end=' ')
input("\nPress <enter> to continue.",)

print("\nWhat day of the week is it?", end = ' ')
day = input()
print("\nWhat month is it?", end = ' ')
month = input()
print("\nWhat year is it?", end = ' ')
year = input()

print(f"\nSo that means that today is a {day} in the month of {month} and the year is {year}.\n")
