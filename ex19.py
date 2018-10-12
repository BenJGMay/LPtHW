# creates our cheese and crackers function which takes 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints the cheese count value
    print(f"You have {cheese_count} cheeses!")
    # prints the boxes of crackers value
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # prints a string
    print("Man that's enough for a party!")
    # prints a string with a line break
    print("Get a blanket.\n")

# prints a string
print("We can just give the function numbers directly:")
# runs the function with 20 and 30 as our arguments
cheese_and_crackers(20, 30)

# prints a string
print("OR, we can use variables from our script")
# sets amounts of cheese to 10
amount_of_cheese = 10
# sets amount of crackers to 50
amount_of_crackers = 50

#Runs the function calling the variables we set above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints a string
print("We can even do math inside too:")
# runs the function, doing math for each argument
cheese_and_crackers(10 + 20, 5 + 6)

# prints a string
print("And we can combine the two, variables and math:")
# runs the function with variables and addition
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
