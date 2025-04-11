def main():
  x = convert_choice(int(input("Scissors, Paper, Rock...")))
  print(x)
  

def convert_choice(choice):
  if choice == 1: 
    return "Rock" 
  elif choice == 2:
    return "Paper"
  elif choice == 3:
    return "Scissors"
  else:
    return "Unknown Choice"

main()


  