
def start():
    end = True
    print(users)
    print(passwords)
    print("Welcome to the program.", end="\n"*2)
    print("1. Login")
    print("2. Register")
    print("3. Quit", end="\n"*2)

    while end:
        question = input("What would you like to do? ").capitalize().strip()
        if question == "Login" or question == "1":
            login()
            end = False
        elif question == "Register" or question == "2":
            register()
            end = False
        elif question == "Quit" or question == "3":
            print("Goodbye and Thank you.") 
            end = False
        else: 
            print("Invaild input. Try again.")
            continue

users = ["sithLord", "d_Vader", "GENERALleia", "grogu", "there_is_no_try", "MyRey", "Luke"]
passwords = ["Ancient enimes r us", "I'm Your Father", "May the Force be with you", "patu", "Yoda", "Jedi", "May the Force be with you"]
new_passwords = []

def login():
    pass

def register():
    pass

start()