text = input("enter a text: ").strip()

if text :
    letter = text.count("a")
    print(letter)
else: 
    print("ERROR : invalid value")