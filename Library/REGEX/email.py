import re
email = str(input("What's your email?")).strip()


if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("invalid")

#REGEX
# ^ start here
# $ end here
# . any character
# * 0 or more of that character
# + 1 or more of that character
# ? 0 or 1, not more
# {x} x repetitions
# {x,y} x-y repetitions
# \ escape character if you wanna use . or ? or something