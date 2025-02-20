def main():
    
    input("Please insert a coin: ")
    
    while True:
        if question_1() == "Yes":
            break
        else: 
            question()
            
def question_1():
    question1 = input("Are you finished? ").capitalize()
    return question1

def question():
    question = input("Please insert a coin: ").capitalize()
    return question

            
            

Boolean = {"No": "False", "Yes": "True"}
        
main()