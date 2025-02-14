def main():
    x = question(input("What do you need? ").casefold())


def question(x):
    if x.startswith("hello"):
        print("No money")
    elif x.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
