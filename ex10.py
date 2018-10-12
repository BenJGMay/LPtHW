tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

my_cats = "\n{} {} {} and I'm actually a {}."
fake_cat = "dog"

print(my_cats.format(tabby_cat, persian_cat, backslash_cat, fake_cat))

print(f"\nAs much as like cats I prefer my {fake_cat}.\n")
