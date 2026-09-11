age = input("enter your age: ").strip()

if age and age.isnumeric():
    age = int(age)
    
    if 0 < age <= 1 :
        print("baby")
    elif 1 < age <= 12 :
        print("childhoode")
    elif 12 < age <= 19:
        print("teenager")
    elif 19 < age <= 35 :
        print("Young")
    elif 35 < age <= 55 :
        print("adulthood")
    elif age > 55 :
        print("old person")
    else :
        print("Error: Your age is invalid.")
else:
    print("ERROR : invalid value")
        