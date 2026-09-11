def table():
    choices = "123456789"
    board = " {} | {} | {} \n {} | {} | {} \n {} | {} | {}"
    return board
    
    
def is_x_o(value):
    if not isinstance(value , (str)):
        raise TypeError(f"{value} is not string")
    if value.upper() in ('X' , 'O'):
        return True
    return False


def get_x_o(prompt=None):
    if prompt is None:
        prompt = "Enter the choose(x|o):"
    while True:
        choice = input(prompt)
        if is_x_o(choice):
            return choice.upper()
        else:
            print(f"{choice} is not a valid choose")


def is_number(value , casting_type):
    try:
        casting_type(value)
        return True
    except ValueError:
        return False


def get_number(casting_type , prompt=None):
    if prompt is None:
        prompt = "Enter a number(1|2|3|...|9):"
    while True:
        number = input(prompt)
        if is_number(number , casting_type):
            number = casting_type(number)
            if not 1 <= number <= 9 :
                print(f"The {number} is not between 1 and 9.")
            else:
                return casting_type(number)
        else :
            print(f"number {number} is not valid")
       
       
def user() :
    choice_first_person = get_x_o()
    if choice_first_person.lower() == "o" :
        return "O" , "X"
    return "X" , "O"
            

def winning(ch ,choices):
    if ch < 5:
        return False
    
    if choices[0] == choices[1] == choices[2]:
        return True
    elif choices[3] == choices[4] == choices[5]:
        return True
    elif choices[6] == choices[7] == choices[8]:
        return True
    elif choices[0] == choices[3] == choices[6]:
        return True
    elif choices[1] == choices[4] == choices[7]:
        return True
    elif choices[2] == choices[5] == choices[8]:
        return True
    elif choices[0] == choices[4] == choices[8]:
        return True
    elif choices[2] == choices[4] == choices[6]:
        return True
    return False
             

def element_placement(choices , board , symbol):
    while True:
        choice_number = get_number(int)
        if choices[choice_number-1].isdigit():
            choices = choices.replace(str(choice_number), symbol)
            print(board.format(*choices))
            return choices
        print("This place is already taken.")


def play_again():
    while True:
        play = input("play again?(y/n):").lower()
        if play == "y":
            return True
        elif play == "n":
            return False
        else:
            print("Please enter y or n.")


def main():
    while True:
        choices = "123456789"
        board = table()

        user1, user2 = user()
        print(board.format(*choices))
        choices = element_placement(choices, board, user1)
        tedad = 1
        game = False
        while tedad < 9 and not game:
                choices = element_placement(choices, board, user2)
                tedad += 1
                if winning(tedad , choices):
                    print("Player 2 wins")
                    game = True
                    break
                
                if tedad >= 9:
                    break
                
                choices = element_placement(choices, board, user1)
                tedad += 1
                if winning(tedad , choices):
                    print("Player 1 wins")
                    game = True
                    break
                
        if not game and tedad>=9 :
            print("draw")    
                
        if not play_again():
            break  

if __name__ == "__main__":
    main()