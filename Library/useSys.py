import sys
try:
    print("hello, my name is", sys.argv[0])
except IndexError:
    print("Please type in your name!")

#sys.exit exits the program
