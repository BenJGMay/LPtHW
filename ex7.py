# prints Mary had a little lamb
print("Mary had a little lamb.")
# prints its fleece was white as x applying snow to that format
print("its fleece was white as {}.".format('snow'))
# prints "And everywhere that Mary went"
print("And everywhere that Mary went.")
print("." * 10) # what'd that do? - Printed 10 fullstops


# This sets end1-12 which will spell out cheeseburger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
#- we get a line break
# Prints "Cheese" and holds the line, somehow
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
# Prints burger
print(end7 + end8 +end9 +end10 + end11 +end12)
