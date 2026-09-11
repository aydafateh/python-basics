def is_number(value , casting_type):
    if not isinstance(value , (int,float,str,complex)):
        raise TypeError(f"valiu {value} is not number")
    if not issubclass(casting_type , (int , float , complex)):
        raise TypeError(f"value {value} is nut number(subclass)")
    try:
        casting_type(value)
        return True
    except:
        return False

def is_operator(operator , casting_type):
    if not isinstance(operator , str):
        raise TypeError(f"opertor {operator} is not valid")
    if operator in ("+",'-',"*","**","/","//" ,"%"):
        return True
    return False


def get_number(casting_type , prompt=None ):
    if prompt == None:
        prompt = "Enter a number"
    while True:
        number = input(prompt)
        if is_number(number , casting_type):
            return casting_type(number)
        else :
            print(f"{number} is not number(get)")


def get_operator(prompt=None):
    if prompt == None:
        prompt = "Enter a operator"
    while True :
        operator = input(prompt)
        if is_operator(operator):
            return operator
        else :
            print(f"{operator} is not operator(get)")



def add(first , second):
    return first + second


def power(first , second):
    return first ** second


def minus(first , second):
    return first - second


def mult(first , second):
    return first * second


def division(first , second):
    if second == 0:
        raise ZeroDivisionError(f"can not division by {second}")
    else :
        return first / second


def remainder(first , second):
    if second == 0:
        raise ZeroDivisionError(f"can not remainder by {second}")
    else :
        return first % second


def int_division(first , second):
    if second != 0:
        return first // second
    else :
        print("not valid")


def main():
    first_number = get_number(float , "first number:")
    second_number = get_number(float , "second number:")
    operator = get_operator("operator:")
    
    if operator == "+":
        result = add(first_number , second_number)
    elif operator == "-":
        result = minus(first_number , second_number)
    elif operator == "**":
        result = power(first_number , second_number)
    elif operator == "/":
        result = division(first_number , second_number)
    elif operator == "*":
        result = mult(first_number , second_number)
    elif operator == "//":
        result = int_division(first_number , second_number)
    else :
        result = remainder(first_number , second_number)
        
    print(f"{first_number} {operator} {second_number} = {result}")
    
if __name__ == "__main__":
    main()