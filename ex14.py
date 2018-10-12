# loads the argv module

from sys import argv
# sets script and username as arguments passed in when script is run
script, user_name, feeling = argv
# sets promp, so we can reference it throughout the scipt
prompt = 'Type your answer: '

# prints statements and asks for user input to set variables

print(f"\nHi {user_name}. I'm the {script} script.")
print("\nI'd like to ask you a few questions.")
print(f"\nDo you like me {user_name}?")
likes = input(prompt)

print(f"\nWhere do you live {user_name}?")
lives = input(prompt)

print("\nWhat kind of computer do you have?")
computer = input(prompt)

print("\nWhat language are you trying to learn?")
language = input(prompt)

# final print. Triple quotes let me break lines in the script?

print(f"""\n
Alright, so you said {likes} about liking me. You live in {lives}. Not sure
where that is. And you have a {computer} computer. Nice. You're trying to learn
{language} and you're feeling {feeling}.
""")
