def main():
    words = input("Say something: ").strip()
    print(convert(words).lstrip("_"))
    
        
        
    

def convert(words):
    for letter in words:
        if letter.isupper():
            words = words.replace(letter, "_" + letter.lower())
    return(words)

main()