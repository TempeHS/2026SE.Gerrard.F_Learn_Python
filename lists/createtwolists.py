necessities = {"1":"Bread", "2":"Water", "3":"Meatballs", "4":"Milk"}
prices = ["4.0", "2.0", "8.0", "5.0"]

def combined_lists():
    print(" |   Item Number |   Items   |   Price   |")
    print(" | ------------- | --------- | --------- |")
    for things in necessities:
        index = int(things) - 1
        print(f" | {things} | {necessities[things]} | {float(prices[index]):.1f} |")

def main():
    print("Current List:",end="\n")
    combined_lists()
    confirm = input("Are you done? ").capitalize()
    if confirm == "Yes":
        print("Lists Updated")
    else:
        add_list()
    

def add_list():
    while True:
        addtolist = input("What do you want to add? ").strip().capitalize()
        new_key = str(int(max(necessities.keys())) + 1)
        necessities[new_key] = addtolist
        new_price = round(float(input("What's the price? ")), 0)
        prices.append(new_price)
        print("New List:",end="\n")
        combined_lists()
        confirm = input("Are you done? ").capitalize()
        if confirm == "Yes":
            break
        else:
            continue

main()
