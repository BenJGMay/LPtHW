# Creates formatter, a string with 4 variables
formatter = "{} {} {} {}"

# prints formatter with .format passing in 4 arguments
print(formatter.format(1, 2, 3, 4))
# prints formatter with .format passing in 4 other arguments
print(formatter.format("one", "two", "three", "four"))
# prints formatter with .format passing in 4 values of True or False
print(formatter.format(True, False, False, True))
# prints formatter with .format calling formatter in to each argument!
print(formatter.format(formatter, formatter, formatter, formatter))
# prints formatter supplying 4 strings in the arguments. The line breaks in code
# look to make it much easier to read - python seems to ignore them
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
