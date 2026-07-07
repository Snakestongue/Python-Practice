
while True:
    inp = input("Enter a password: ")

    lower=False
    upper = False
    digit = False
    space = False
    special = False
    specials = "$#@_!"

    for i in inp:
        if 'a' <= i <= 'z':
            lower = True
        elif 'A' <= i <= 'Z':
            upper = True
        elif '0' <= i <= '9':
            digit = True
        elif i in specials:
            special = True
        elif i == ' ':
            space = True
    valid = True
    if not lower:
        print("Need lowercase letter")
        valid = False
    if not upper:
        print("Need uppcase letter")
        valid = False
    if not digit:
        print("Need number")
        valid = False
    if not special:
        print("Need special letter")
        valid = False
    if space:
        print("has a space")
        valid = False
    if len(inp) < 6:
        print("Too short")
        valid = False
    if len(inp) > 12:
        valid = False
        print("Too long")

    if valid:

        print("all good")
        break
