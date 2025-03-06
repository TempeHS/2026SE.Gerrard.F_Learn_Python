
def main():
    total = 0
    while total < 50:
        x = convert(question())
        if x not in [25, 10, 5]:
            print("Not a valid coin, please insert another.")
        else:
            total += x
            if total < 50:
                print("Please insert more coins, you current total is", total)
            elif total >= 50:
                print(f"Thank you for your purchase, your change is {total - 50} cents.")


def question():
    question = input("Please insert a coin: ").strip()
    return question

def convert(x):
    return int(x)

main()

#Used co-pilot to reorganise the order of my code