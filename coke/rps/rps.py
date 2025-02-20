def main():
    player_user()
    player_choice()
    
def player_user():
    name = input("What's your username? ").title()
    return print(name)
    
def player_choice():
    move = input("Play a move: ").title()
    if moves == False:
        print("Not a valid option")
    return print(move)

def random_choice():
    return random.radiant(1, 3) 
    


moves = {"Rock": "1", "Paper": "1", "Scissors": "1"}

main()