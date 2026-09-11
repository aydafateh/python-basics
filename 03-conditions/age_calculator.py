date_birth = input("enter your birthday (yyyy/mm/dd): ").strip()
today = input("enter today date (yyyy/mm/dd): ").strip()
birth = date_birth.split("/")
today = today.split("/")

if birth[0].isdigit :
    year_birth = int(birth[0])
    if today[0].isdigit:
        year_today = int(today[0])
        year_age = year_today - year_birth
        
        if birth[1].isdigit:
            month_birth = int(birth[1])
            if today[1].isdigit:
                month_today = int(today[1])
                if month_birth > month_today :
                    month_age = month_today - month_birth
                    year_age = year_age - 1
                    month_age = 12 + month_age
                else :
                    month_age = month_today - month_birth
                
                if birth[2].isdigit:
                    day_birth = int(birth[2])
                    if today[2].isdigit:
                        day_today = int(today[2])
                        
                        if day_birth > day_today :
                            month_age = month_age - 1
                            day_age = day_today - day_birth
                            day_age = 30 + day_age
                            print(year_age,"year",month_age,"month",day_age,"day")
                        else :
                            day_age = day_today - day_birth
                            print(year_age,"year",month_age,"month",day_age,"day")
                            
                    else: print("Error : You entered today's date incorrectly.")
                else: print("Error : The birthday is wrong")
            else: print("Error :You entered the current month's date incorrectly.")
        else: print("Error:You entered the wrong month of birth.")
    else : print("Error :This year's number is wrong")
else : print("Error :The year of birth is wrong.")