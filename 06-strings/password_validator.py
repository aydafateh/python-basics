char_lower = "abcdefghijklmnopqrstuvwxyz"
char_uper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
character = "@#$%&*!?"

char_lower = set(char_lower)
char_uper = set(char_uper)
number = set(number)
character = set(character)

password_user = input("Enter your password:")

if len(password_user) >= 8 :
    password_user = set(password_user)
    if len(password_user & character) >= 1:
        print("Use special characters.")
    else: 
        print("No special characters.")
        
    if len(password_user & char_uper) >=1 :
        print("Use capital letters.")
    else: 
        print("At least one capital letter is missing.")
    if len(char_lower & password_user) >= 1:
        print("Use lowercase letters.")
    else: 
        print("It does not have at least one lowercase letter.")
        
    if len(number & password_user) >= 1:
        print("Used the number.")
    else: print("Does not have at least one number")
else:print("Not 8 characters")