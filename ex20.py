# imports the argv module
from sys import argv

# sets the two command line arguments as script and input_file
script, input_file = argv

# Create a function that takes f as an argument
def print_all(f):
    #prints f in read mode
    print(f.read())

# Creates a rewind function that takes f as an argument
def rewind(f):
    # We seek to the very begining (byte 0) of f
    f.seek(0)

# creates a function that takes "line count" and "f" as arguments
def print_a_line(line_count, f):
    # prints line count and reads the current line for f, ending at the \n
    print(line_count, f.readline())

# creates the current file variable, which the open file object of input file
current_file = open(input_file)

# prints a string
print("First let's print the whole file:\n")

#runs the print all function on current file - i.e runs print/read on it
print_all(current_file)

# prints another string
print("Now let's rewind, kind of like a tape.")

# Runs rewind on current file, taking our position to 0
rewind(current_file)

# prints a string
print("Let's print three lines:")

# sets a variable of current_line to 1
current_line = 1
# prints 1 and the current position to next line break (line 0-1)
print_a_line(current_line, current_file)

# prints 2 and the current position to next line break (line 1-2)
current_line += 1
print_a_line(current_line, current_file)

# prints 3 and the current position to next line break (line 2-3)
current_line += 1
print_a_line(current_line, current_file)
