first_name = input("enter your first name: ").strip()
first_name = first_name.replace(" " ,"")
if first_name and first_name.isalpha() :
    last_name = input("enter your last name: ").strip()
    last_name = last_name.replace(" ","")
    if last_name and last_name.isalpha() :
        user_name = input("enter a user name: ").strip()
        
        if user_name and user_name.isidentifier() :
            phone_number = input("enter your phone number: ").strip()
            
            if (phone_number 
                and phone_number.startswith("09")
                and phone_number.isdigit()
                and len(phone_number) == 11
            ):
                phone_number = int(phone_number)
                
                user = {
                    "first name" : first_name,
                    "last name" : last_name,
                    "user name" : user_name,
                    "phone number" : phone_number
                }
                
                print(user)
            else :
                print("ERROR : invelid phone number")
        else:
            print("ERROR : invelid user name")
    else:
        print("ERROR : invelid last name")
else:
    print("ERROR : invelid first name")