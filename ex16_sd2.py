# imports the argument module from sys
from sys import argv

script, filename = argv

print(f"We're going read {filename}.\n")

print("Opening the file...\n")
target = open(filename, 'r')

print(target.read())

target.close()
