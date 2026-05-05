def main():
    name = input("What's your name? ")
    print(hello(name))
def hello(abc="world"):
    return f"Hello {abc}"



if __name__ == "__main__":
    main()