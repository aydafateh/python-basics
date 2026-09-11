number = input("enter a float number: ").strip()
if number :
    number_split = number.split(".")
    if len(number_split) == 2:
        if number_split[0].isdigit() :
            if number_split[1].isdigit() :
                
                number_str = str(number_split[0] + "." + number_split[1])
                print(f"string : '{number}'")
                number = float(number_str)
                print(f"float : {number}")
                
                number_int = int(number)
                print(f"integer : {number_int}")
                
                number_tuple = tuple(number_str)
                print(f"tuple : {number_tuple}")
                
                number_list = list(number_str)
                print(f"list : {number_list}")
                
                number_set = set(number_str)
                print(f"set : {number_set}")
                
            else:
                print("ERROR : invalid num")
                
        else:
            print("ERROR : invalid num")
            
    else:
        print("ERROR : not float number")
else:
    print("ERRORRRRRRR")                