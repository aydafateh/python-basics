board = ["1","2","3","4","5","6","7","8","9"]
condition = True
while condition:
    while True:
        select_first_person = input("enter choice(O|X):")
        if select_first_person.upper() == "O":
            user1 , user2 = "O" , "X"
            break
        elif select_first_person.upper() == "X":
            user1 , user2 = "X" ,"O"
            break
        else:
            print("Error: invalid choice")
            
    while True:            
        choice_user1 = input("choice place user1 (1|2|3|4|5|6|7|8|9):")
        if choice_user1 in "123456789" and len(choice_user1)==1:
            index = int(choice_user1) - 1
            if board[index] not in ["O","X"]:
                board[index] = user1
                print(f"{board[0]} {board[1]} {board[2]} \n{board[3]} {board[4]} {board[5]} \n{board[6]} {board[7]} {board[8]}")
                break
            else:
                print("place is already token")
        else:
            print("Error: invalid number")
    for i in range(4):
        while True:
            choice_user2 = input("choice place user2 (1|2|3|4|5|6|7|8|9):")
            if choice_user2 in "123456789" and len(choice_user2) == 1:
                index = int(choice_user2) - 1
                if board[index] not in ["O","X"]:
                    board[index] = user2
                    print(f"{board[0]} {board[1]} {board[2]} \n{board[3]} {board[4]} {board[5]} \n{board[6]} {board[7]} {board[8]}")
                    if (board[0] == board[1] == board[2] == "X") or\
                        (board[3] == board[4] == board[5] == "X") or\
                        (board[6] == board[7] == board[8] == "X") or\
                        (board[0] == board[3] == board[6] == "X") or\
                        (board[1] == board[4] == board[7] == "X") or\
                        (board[2] == board[5] == board[8] == "X") or\
                        (board[0] == board[4] == board[8] == "X") or\
                        (board[2] == board[4] == board[6] == "X"):
                        print("Won (X)")
                        condition = False
                    elif board[0] == board[1] == board[2] == "O" or\
                        (board[3] == board[4] == board[5] == "O") or\
                        (board[6] == board[7] == board[8] == "O") or\
                        (board[0] == board[3] == board[6] == "O") or\
                        (board[1] == board[4] == board[7] == "O") or\
                        (board[2] == board[5] == board[8] == "O") or\
                        (board[0] == board[4] == board[8] == "O") or\
                        (board[2] == board[4] == board[6] == "O"):
                        print("Won (O)")
                        condition = False
                    break
                else:
                    print("place is already token")
            else:
                print("Error: invalid number")
                
        if not condition:
            break
                
        while True:            
            choice_user1 = input("choice place user1 (1|2|3|4|5|6|7|8|9):")
            if choice_user1 in "123456789" and len(choice_user1)==1:
                index = int(choice_user1) - 1
                if board[index] not in ["O","X"]:
                    board[index] = user1
                    print(f"{board[0]} {board[1]} {board[2]} \n{board[3]} {board[4]} {board[5]} \n{board[6]} {board[7]} {board[8]}")
                    if (board[0] == board[1] == board[2] == "X") or\
                        (board[3] == board[4] == board[5] == "X") or\
                        (board[6] == board[7] == board[8] == "X") or\
                        (board[0] == board[3] == board[6] == "X") or\
                        (board[1] == board[4] == board[7] == "X") or\
                        (board[2] == board[5] == board[8] == "X") or\
                        (board[0] == board[4] == board[8] == "X") or\
                        (board[2] == board[4] == board[6] == "X"):
                        print("Won (X)")
                        condition = False
                    elif board[0] == board[1] == board[2] == "O" or\
                        (board[3] == board[4] == board[5] == "O") or\
                        (board[6] == board[7] == board[8] == "O") or\
                        (board[0] == board[3] == board[6] == "O") or\
                        (board[1] == board[4] == board[7] == "O") or\
                        (board[2] == board[5] == board[8] == "O") or\
                        (board[0] == board[4] == board[8] == "O") or\
                        (board[2] == board[4] == board[6] == "O"):
                        print("Won (O)")
                        condition = False
                    break
                else:
                    print("place is already token")
            else:
                print("Error: invalid number")
                    
        if not condition:
            break
    while True:
        nexted = input("edame?(Y|N):")
        if nexted.upper() == "Y" :
            print("OK")
            board = ["1","2","3","4","5","6","7","8","9"]
            condition = True
            break
        elif nexted.upper() == "N":
            print("by by")
            condition = False
            break
        else:
            print("Error : please enter Y or N (barname baste mishe)")
            exit()