text = input("Enter the text: ")
sentences = text.split(".") + text.split("!") + text.split("?") + text.split(";")

print(len(sentences)-4)