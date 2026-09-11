number = input("Enter the number(at least 2):")
if len(number) >= 2:
    numbers = list(number)
    numbers.sort(reverse=True)
    larg = "".join(numbers)
    print(larg)
else:
    print("Error:number must have at least 2 digits")
