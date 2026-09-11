fact = 1

while True:
    try:
        number = input("Enter the factorial number (enter 0 to exit):")
        if number.isdigit:
            number = int(number)
            if number == 0:
                break
            elif number < 0:
                print("ERROR: Enter a positive number")
            
            for num in range(1 , number+1):
                fact = fact * num
            print(f"{number}! = {fact}")
    except ValueError:
        print("Error number")