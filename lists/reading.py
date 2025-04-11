name = ["man", "slave", "dog", "eater"]
password = ["monkey", "master", "cat", "food"]

def change_password():
    while True:
        user = input("What's your username? ")

        if user not in name: 
            print("Your user does not exist. ")
            continue

        else:
            break
    
    for i in range(len(name)):
        if user in name:
            user == i - 1
            print(user)
    
    

change_password()
