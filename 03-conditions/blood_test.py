RBC = input("Enter the RBC (گلبول قرمز):")
Hb = input("Enter the Hb (هموگلوبین):")
Hct = input("Entre the Hct (هماتوکریت):")
WBC = input("Enter the WBC(گلبول سفید):")
Platelet = input("Enter the Plateltet (پلاکت):")

RBC = RBC.replace(".","")
Hb = Hb.replace(".","")
if RBC.isdigit() and Hb.isdigit() and Hct.isdigit() and WBC.isdigit() and Platelet.isdigit():
    RBC = float(RBC)
    Hb = float(Hb)
    Hct = float(Hct)
    WBC = float(WBC)
    Platelet = float(Platelet)
    
    if RBC > 61 :
        print("Increased red blood cells")
    elif 42 <= RBC <= 61 :
        print("normal red blood cells")
    elif RBC < 42 :
        print("Decreased red blood cells")
    else : 
        print("Error : The entered number is not in the range.")
        
    if Hb > 172 :
        print("Increased blood hemoglobin")
    elif 121 <= Hb <= 172 :
        print("normal blood hemoglobin")
    elif Hb < 121 :
        print("Decreased blood hemoglobin")
    else : 
        print("Error : The entered number is not in the range.")
        
    if Hct > 52 :
        print("Increased hematocrit")
    elif 36 <= Hct <= 52 :
        print("Normal hematocrit")
    elif Hct < 36 :
        print("Decreased hematocrit")
    else : 
        print("Error : The entered number is not in the range.")
        
    if WBC > 11000:
        print("Increased white blood cell")
    elif 4500 <= WBC <= 11000 :
        print("Normal white blood cell")
    elif WBC < 4500 :
        print("Decreased white blood cell")
    else : 
        print("Error : The entered number is not in the range.")
        
    if Platelet > 450000 :
        print("Increased blood platelets")
    elif 150000 <= Platelet <= 450000 :
        print("Normal blood platelets")
    elif Platelet < 150000:
        print("Decreased blood platelets")
    else : print("Error :The entered number is not in the range.")
else: print("Error :You did not enter a number")