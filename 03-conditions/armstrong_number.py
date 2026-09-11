
num = input("Enter a number: ")
if num.isdigit:
    number = len(num)
    sum_of_powers = 0

    for digit in num:
        sum_of_powers += int(digit) ** number

    if sum_of_powers == int(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is NOT an Armstrong number")
else:
    print("ERROR:intiger")