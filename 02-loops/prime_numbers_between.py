number1 = input("enter a first number:")
number2 = input("enter a second number:")

numbers_prim = []

try:
    number1 = int(number1) 
    number2 = int(number2)
    
    if number1 > number2:
        number1, number2 = number2, number1
    
    for num in range(number1 , number2 + 1):
        if num < 2:
            continue
        is_prime = True
        
        for i in range(2 , int(num**0.5)+1):
            if num % i == 0 :
                is_prime = False
                break
            
        if is_prime:
            numbers_prim.append(num)
    print(numbers_prim)
except ValueError:
    print("ERROR: Please enter valid integer numbers!")