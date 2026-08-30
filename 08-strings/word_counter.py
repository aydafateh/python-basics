sentence = input("enter the sentance: ")

if sentence :
    sentence = sentence.split(" ")
    len_word = 0
    
    for word in sentence:
        if word.isalpha() :
            len_word += 1
            
    print(len_word)
    
else:
    print("ERROR : invalid value")