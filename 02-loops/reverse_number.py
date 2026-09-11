number = input("Enter a number:")
reverse = 0
if number and number.isnumeric():
    number = int(number)
    while number> 0 :
        num = number %10
        reverse = reverse * 10 + num
        number = number // 10
        
    print(f"reverse: {reverse}")
else :
    print("Error:numeric")