choices = "123456789"
board = "{} {} {}\n" "{} {} {}\n" "{} {} {}"
table = board.format(*choices)
print(table)  

select_first_user = input("Please choose(O,X):")
if select_first_user == "O":
    user1 = "O"
    user2 = "X"
else:
    user1 = "X"
    user2 = "O"


choices_user1 = input("Tell the chosen place user(O):")
if choices_user1.isdigit():
    if choices_user1 in choices and len(choices_user1) == 1:
        choices = choices.replace(choices_user1, user1)
    else:
        print("Error")
    choices_user1 = input("Tell the chosen place user(X):")
    
    if choices_user1.isdigit():
        if choices_user1 in choices and len(choices_user1) == 1:
            choices = choices.replace(choices_user1, user2)
        else: print("Error")
    else:
        print("Error: Invalid place")
else:
    print("Error: Invalid place")
    
table = board.format(*choices)
print(table)

choices_user1 = input("Tell the chosen place user(O):")

if choices_user1.isdigit():
    if choices_user1 in choices and len(choices_user1) == 1:
        choices = choices.replace(choices_user1, user1)
    else:
        print("Error")
    choices_user1 = input("Tell the chosen place user(X):")
    
    if choices_user1.isdigit():
        if choices_user1 in choices and len(choices_user1) == 1:
            choices = choices.replace(choices_user1, user2)
        else: 
            print("Error")
    else:
        print("Error: Invalid place")
else:
    print("Error: Invalid place")
    
table = board.format(*choices)
print(table)

choices_user1 = input("Tell the chosen place user(O):")
if choices_user1.isdigit():
    if choices_user1 in choices and len(choices_user1) == 1:
        choices = choices.replace(choices_user1, user1)
    else:print("Error")
    choices_user1 = input("Tell the chosen place user(X):")
    
    if choices_user1.isdigit():
        if choices_user1 in choices and len(choices_user1) == 1:
            choices = choices.replace(choices_user1, user2)
        else:
            print("Error")
    else:
        print("Error: Invalid place")
else:
    print("Error: Invalid place")
    
table = board.format(*choices)
print(table)

if choices[0] == choices[1] == choices[2] and choices[0] in "OX":
    print(choices[0], "won")
    
elif choices[3] == choices[4] == choices[5] and choices[3] in "OX":
    print(choices[3], "won")
    
elif choices[6] == choices[7] == choices[8] and choices[6] in "OX":
    print(choices[6], "won")
    
elif choices[0] == choices[3] == choices[6] and choices[0] in "OX":
    print(choices[0], "won")
    
elif choices[1] == choices[4] == choices[7] and choices[1] in "OX":
    print(choices[1], "won")
    
elif choices[2] == choices[5] == choices[8] and choices[2] in "OX":
    print(choices[2], "won")
    
elif choices[0] == choices[4] == choices[8] and choices[0] in "OX":
    print(choices[0], "won")
    
elif choices[2] == choices[4] == choices[6] and choices[2] in "OX":
    print(choices[2], "won")
    
else:
    choices_user1 = input("Tell the chosen place user(O):")
    if choices_user1.isdigit():
        if choices_user1 in choices and len(choices_user1) == 1:
            choices = choices.replace(choices_user1, user1)
        else:
            print("Error")
        choices_user2 = input("Tell the chosen place user(X):")
        
        if choices_user2.isdigit():
            if choices_user2 in choices and len(choices_user2) == 1:
                choices = choices.replace(choices_user2, user2)
            else: print("Error")
        else:
            print("Error: Invalid place")
    else:
        print("Error: Invalid place")
        
    table = board.format(*choices)
    print(table)
    if choices[0] == choices[1] == choices[2] and choices[0] in "OX":
        print(choices[0], "won")
        
    elif choices[3] == choices[4] == choices[5] and choices[3] in "OX":
        print(choices[3], "won")
        
    elif choices[6] == choices[7] == choices[8] and choices[6] in "OX":
        print(choices[6], "won")
        
    elif choices[0] == choices[3] == choices[6] and choices[0] in "OX":
        print(choices[0], "won")
        
    elif choices[1] == choices[4] == choices[7] and choices[1] in "OX":
        print(choices[1], "won")
        
    elif choices[2] == choices[5] == choices[8] and choices[2] in "OX":
        print(choices[2], "won")
        
    elif choices[0] == choices[4] == choices[8] and choices[0] in "OX":
        print(choices[0], "won")
    
    elif choices[2] == choices[4] == choices[6] and choices[2] in "OX":
        print(choices[2], "won")
        
    else:
        choices_user1 = input("Tell the chosen place user(O):")
        if choices_user1.isdigit():
            if choices_user1 in choices and len(choices_user1) == 1:
                choices = choices.replace(choices_user1, user1)
            else:print("Error")
        else:
            print("Error: Invalid place")
    
    