def main():
    user = question(input("What's the name of your file? ")).strip().lower()
    

def question(x):
    if x.endswith(".jpg"):
        print("image/jpg")

    elif x.endswith("jpeg"):
        print("image/jpeg")

    elif x.endswith("png"):
        print("image/png")
    
    elif x.endswith(".pdf"):
        print("documents/pdf")

    elif x.endswith(".gif"):
        print("image/gif")

    elif x.endswith(".zip"):
        print("application/zip")
    
    elif x.endswith(".txt"):
        print("plain.txt")

    else:
        print("application/octet-stream")
    return x




main()