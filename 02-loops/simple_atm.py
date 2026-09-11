balance = 100000
while True :
    print("ATM machine \n 1) View Balance \n 2) Withdraw \n 3) Deposit \n 4) Logout")
    choice = input("Enter your selection:")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            print(f"Your account balance:{balance}")
        elif choice == 2:
            withdrawal_amount = input("Enter the withdrawal amount:")
            if withdrawal_amount.isdigit():
                withdrawal_amount = int(withdrawal_amount)
                if withdrawal_amount <= balance:
                    balance -= withdrawal_amount
                    print(f"Amount {withdrawal_amount} withdrawn \n New inventory {balance}")
                else :
                    print("ERROR :Insufficient inventory")
            else :
                print("ERROR : isdigit")
        elif choice == 3:
            deposit = input("Enter the deposit amount:")
            if deposit.isdigit():
                deposit = int(deposit)
                balance += deposit
                print(f"Amount {deposit} was deposited. \n New inventory {balance}")
            else :
                print("Error :isdigit")
        elif choice == 4:
            print("Exit the program")
            break
        else:
            print("Invalid number")