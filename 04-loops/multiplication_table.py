user_number = input("Enter a number: ").strip()

if user_number and user_number.isnumeric():
    user_number = int(user_number)
    
    for number in range(0,11):
        mult = number * user_number
        print(f"{number} * {user_number} = {mult}")
        
        number += 1      
else: 
    print("ERROR : invalid value")