# This creates a variable called types of people and gives it a value of 10
types_of_people = 10
# This creates a variable string that references the types_of_people value
x = f"There are {types_of_people} types of people."

# This creates variable string called binary and sets it to "binary"
binary = "binary"
# This sets a variable string called do_not and sets it to "don't"
do_not = "don't"
# This sets a variable string called Y that includes the above two variable strings
y = f"Those who know {binary} and those who {do_not}."

#This prints X
print(x)
# This prints Y
print(y)

# This prints "I said:"" and then the string X
print(f"I said: {x}")
# This prints "I also said" and then the string Y
print(f"I also said: '{y}'")

# This create variable called hilarious and sets it to False
hilarious = False
# This sets a variable string called joke_evaluation and asks if the joke is funny. I don't know what the angular brackets are for.
joke_evaluation = "Isn't that joke so funny?! {}"

# This prints joke_evaluation and feeds the hilarious value into the angular brackets above, I think
print(joke_evaluation.format(hilarious))

# Part one of a a variable string
w = "This is the left side of..."
# The other part
e = "a string with a right side."

# Prints the two strings above
print(w + e)
