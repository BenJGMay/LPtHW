from sys import argv

script, filename = argv

print(f"\nWe're going to erase {filename}.")
print("\nIf you don't want that, hit CTRL-C (^C)." )
print("\nIf you do want that, hit RETURN.")

input("?")

print("\nOpening the file...")
target = open(filename, 'w')

print("\nTruncating the file. Goodbye!")
# not actually needed as write mode does this automatically - we would need it
# if we were using append (a)
#target.truncate()

print("\nNow I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("\nI'm going to write these to the file.")

#One way to do this is one line
#target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#another way to do this in one line
target.write(f"{line1}\n{line2}\n{line3}\n")

# a way to do it many lines
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("\nAnd finally, we close it\n")
target.close()
