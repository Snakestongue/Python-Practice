user = str(input("Type in a valid username:  "))
if len(user) > 12:
    print("Inalid")
elif not user.find(" ") == -1:
    print("Invalid")
elif not user.isalpha():
    print("Invalid")
else:
    print(f"Welcome {user}")
