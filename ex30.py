# sets people
people = 30
# sets cars
cars = 40
# sets trucks
trucks = 15

# if is true here
if cars > people:
    # so we print this line
    print("We should take the cars.")
elif cars < people:
    # if cars was greater than people we would print this
    print("We should not take the cars.")
else:
    # if neither of the above is true we print this
    print("We can't decide.")

# if it is true that trucks are greater than cars
if trucks > cars:
    # we print that's too many trucks
    print("That's too many trucks.")
    # of it is false we print the below
elif trucks < cars:
    print("Maybe we could take the trucks.")
    # under any other condition we print the below
else:
    print("We still can't decide.")

# if it is true that people are greater than trucks
if people > trucks:
    # we print the below
    print("Alright, let's just take the trucks.")
# Otherwise we print the below
else:
    print("Fine, let's stay home then.")

# if cars is the highestr value we print
if cars > people or trucks < cars:
    print("We have plenty of cars.")
# otherwise
else:
    print("We have either more people or trucks than cars")

# if its not true that people is higher than one of the other values we print
if not (cars < people or trucks < people):
    print("We have more people than one of the values of cars or trucks.")
# otherwise
else:
    print("Less people than either cars or trucks!")
