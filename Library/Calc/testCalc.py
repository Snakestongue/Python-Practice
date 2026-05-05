def main():
    while True:
        try:
            x = int(input("What's x? "))
            break
        except ValueError:
            print("Not a number")
    print(x, "squared is", square(x))


def square(x):
    return x+x