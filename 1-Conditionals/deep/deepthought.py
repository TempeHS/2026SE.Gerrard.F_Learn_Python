def bigquestion():
    x = answer(input("What's the answer to the Great Question of Life? ")).lower()

    

def answer(p):
    if p == "42":
        print("Yes")
    elif p == "forty-two":
        print("Yes")
    elif p == ("forty two"):
        print("Yes")
    else: 
        print("No")
    return p

bigquestion()