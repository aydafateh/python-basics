User_email = input("Enter your email:")

if User_email.endswith("@gmail.com"):  
    User_email = User_email.split("@")  
    if User_email[0].isidentifier():
        print("The user's email is valid")
    else:
        print("Error:The user's email is invalid.")
else:
        print("The user's email is invalid.")  