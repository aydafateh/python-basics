MCI = ("996","995","994","993","992","991","990","91")
Irancel =("930","931","932","933","934","935","936","937","938","939",
          "900","901","901","902","903","904","905","941")
Rightel = ("920","921","922","923")

number_phone = input("Enter your phone number:")
if number_phone.isdigit:
    if len(number_phone) == 11 or len(number_phone) == 13 or len(number_phone) == 12:
        if number_phone.startswith("0"):
            number_phone = number_phone.replace("0","",1)
            if number_phone.startswith(MCI):
                print("Mobile phone is valid")
            elif number_phone.startswith(Irancel):
                print("Mobile phone is valid")
            elif number_phone.startswith(Rightel):
                print("Mobile phone is valid")
            else: print("Error : Mobile phone is invalid.")
        
        elif number_phone.startswith("+98"):
            number_phone = number_phone.replace("+98","",1)
            if number_phone.startswith(MCI):
                print("Mobile phone is valid")
            elif number_phone.startswith(Irancel):
                print("Mobile phone is valid")
            elif number_phone.startswith(Rightel):
                print("Mobile phone is valid")
            else: print("Error : Mobile phone is invalid.")
            
        elif number_phone.startswith("98"):
            number_phone = number_phone.replace("98","",1)
            print(number_phone)
            if number_phone.startswith(MCI):
                print("Mobile phone is valid")
            elif number_phone.startswith(Irancel):
                print("Mobile phone is valid")
            elif number_phone.startswith(Rightel):
                print("Mobile phone is valid")
            else: print("Error : Mobile phone is invalid.")
            
        else: print("Error:It is not an Iranian number")
    else: print("Error :The length of the number is incorrect")
else: print("Error: Enter a number")