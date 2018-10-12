# prints a string
print("Let's practice everything.")
# Uses escape characters to display apostophies and a backslash
print('You\'d need to know \'bout escapes with \\ that do:')

print('\n newlines and \t tabs')
# uses escape characters to print a new line and tab in

# sets a variable. Tripe """ let us do a multi line string that
# accepts escape characters
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# prints Hyphen lines, the poem variable, and then hyphen lines
print("--------------")
print(poem)
print("--------------")


# creates a variable that is equal to some math
five = 10 - 2 + 3 - 6
# prints a string including the above variable
print(f"This should be five: {five}")

# creates the secret_formula function
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    # we return the new value of these variables to the program
    return jelly_beans, jars, crates


#sets start_point
start_point = 10000
# sets these variables to the returned values from the secret_formula function
beans, jars, crates = secret_formula(start_point)

# remember this is another way to format a string
# we use .format to plug start_point to the {}
print("With a starting point of: {}".format(start_point))
# it's just like starting with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# sets a new value for start point equal to the old one / 10
start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, jars {}, and {} crates.".format(*formula))
