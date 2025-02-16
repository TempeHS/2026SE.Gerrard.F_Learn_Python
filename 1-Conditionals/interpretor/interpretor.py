def main():
    val_x = float(input("I can solve anything, what's the value for x: "))
    val_y = float(input("What's the value for y: "))
    z = input("What operation should I do: ")
    
    if z == "-":
        ans = (val_x - val_y)
    elif z == "+":
        ans = (val_x + val_y)
    elif z == "*":
        ans = (val_x * val_y)
    elif z == "/":
        ans = (val_x / val_y)
    else:
        print("I can't do that. ")
    
    print(f"{ans:.1f}")

def val_x(x):
    return x

def val_y(y):
    return y

main()




    
