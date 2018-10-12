#We import the argv module
from sys import argv
# we set script and filename to arguments set when the script is run
script, filename = argv
# We set txt to an open "file object" - the argument the user put in
txt = open(filename)
#We print a line of text. I have added a line break for readability
print(f"\nHere's your file {filename}:")
# We print the txt variable which has the read function applied to it
print("\n")
print(txt.read())
# We print another line of text
print("\nType that filename again:")
# we set file_again to a user input as opposed to an argument
file_again = input("> ")
# we create txt_again and set it a file object for file_again
txt_again = open(file_again)
print("\n")
# We print txt_again with the read function applied to it.
print(txt_again.read())

txt.close()
txt_again.close()
