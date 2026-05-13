def addNotes(abc):
    try:
        with open("notes.txt", "a") as file:
            file.write(f"{abc}\n")
    except:
        with open ("notes.txt", "w") as file:
            print("File made. Try again!")

def readNotes():
    try:
        with open("notes.txt", "r") as file:
            for x in file:
                print (f"{x.rstrip()}")
    except:
        with open ("notes.txt", "w") as file:
            print("File made. Try again!")

def main():
    inp = None
    while inp!="d":
        inp = input("Would you like add notes(a) or see your notes (s)? ")
        if inp.lower() == 'a':
            print("Enter your notes below!")
            notes = input("")
            addNotes(notes)
            print("Added!")
        elif inp.lower() == 's':
            readNotes()
        elif inp.lower() == 'd':
            break
        else:
            print("Not an option! Try again: ")
    print("Thanks for using this!")
    