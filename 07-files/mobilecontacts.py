import os
import platform
from time import sleep

def clear():
    system_name = platform.system()
    if system_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def validate_password(password):
    if len(password) != 8:
        return False, f"Error: password must be exactly 8 characters (got {len(password)})"
    if not any(char in password for char in ("@", "#")):
        return False, "Error: Password must contain @ or #"
    if not password.isascii():
        return False, "Password must be ASCII characters only"
    return True, ""


def validate_username(username):
    if not username.isidentifier():
        return False, f"'{username}' is not a valid username identifier"
    return True


def validate_phone(phone):
    if phone.startswith("+98"):
        simple = phone[3:]
        if simple.isdigit() and len(simple) == 10:
            return True
        return False, f"{phone} is not valid phone number"
    if len(phone) != 11:
        return False, f"{phone} not valid phone (must be 11 digits)"
    if not phone.isdigit():
        return False, f"{phone} not valid phone (digits only)"
    return True


def validate_fullname(fullname):
    fullname = fullname.strip()
    if not fullname:
        return False, "fullname cannot be empty"
    if not fullname.isalpha():
        return False, f"{fullname} contains invalid characters"
    return True


def validate_email(email):
    email = email.strip()
    if not email.endswith("@gmail.com"):
        return False, "Email must end with @gmail.com"
    part = email.split("@")
    if not part[0].isidentifier():
        return False, "Invalid email username part"
    return True


def get_username():
    while True:
        username = input("enter username:")
        username = username.strip()
        if validate_username(username):
            return username
        print("Error:invalid username")
        

def get_password():
    while True:
        password = input("Enter password (@,#,digits,letters, length 8): ").strip()
        valid, message = validate_password(password)
        if valid:
            return password
        print(message)
        
    
def get_fullname():
    while True:
        first_name = input("enter first name:")
        first_name = first_name.strip()
        if not validate_fullname(first_name):
            print("Erorr: invalid first name")
            continue
        
        last_name = input("enter last name:")
        last_name = last_name.strip()
        if not validate_fullname(last_name):
            print("Error:invalid last name")
            continue
        return first_name , last_name

        
def get_phone_number():
    while True:
        phone = input("enter phone number")
        phone = phone.strip()
        if validate_phone(phone):
            return normalize_phone(phone)
        print("error: invalid phone")


def get_email():
    while True:
        email = input("enter email:")
        email = email.strip()
        if validate_email(email):
            return email
        print("Error : invalid email")
        
        
def get_contact():
    first_name , last_name = get_fullname()
    phone = get_phone_number()
    email = get_email()
    return first_name, last_name, phone , email


def get_search():
    query = input("enter name or phone number to search:")
    query = query.strip()
    return query.lower()

def normalize_phone(phone):
    if phone.startswith("+98"):
        return phone.replace("+98", "0")
    return phone

def r_file_users():
    users = []
    try:
        file = open("users.txt", "r")
        for line in file:
            line = line.strip()
            if line :
                users.append(line)
        return users
    except:
        return []
    
def r_file_contact():
    contacts = []
    try:
        file = open("contacts.txt" , "r")
        for line in file:
            line = line.strip()
            if line:
                contacts.append(line)
    except:
        print("_")
    return contacts


def save_user(username, password):
    try:
        file = open("users.txt", "a")
        file.write(f"{username}:{password}\n")
        return True
    except:
        return False
    
    
def save_contact(first_name, last_name, phone, email):
    try:
        file = open("contacts.txt", "a")
        file.write(f"{first_name} {last_name} {phone} {email}\n")
        return True
    except :
        return False
    

def user_exists(username):
    users = r_file_users()
    for line in users:
        if ":" in line:
            user = line.split(":" , 1)[0]
            if user == username:
                return True
    return False


def get_user_pass(username):
    users = r_file_users()
    for line in users:
        if ":" in line:
            line = line.split(":" , 1)
            user = line[0].strip()
            password = line[1].strip()
            if user == username:
                return password
    return None


def register_new_user():
    print("______\nregister new user\n______")
    username = get_username()
    if user_exists(username):
        print("Error : username already exists")
        sleep(2)
        return False
    password = get_password()
    if save_user(username , password):
        print("registeration successful")
        sleep(2)
        return True
    return False
    

def login_user():
    print("______\nlogin\n______")
    username = input("enter username:").strip()
    password = input("enter password:").strip()
    password_save = get_user_pass(username)
    if password_save == password:
        print("login succsesful")
        sleep(2)
        return True
    print("invalid username or password")
    sleep(2)
    return False

def display_menu(options, prompt="menu: "):
    clear()
    print(f"______\n{prompt}\n______")
    for option in options:
        print(f"{option}. {options[option]}")

def get_menu_choice(
    menu, 
    prompt="enter your choice:"
):
    error = False
    while True:
        display_menu(menu)
        if error:
            print("Error: Please enter a valid option")
            display_menu(menu)
        choice = input(prompt)
        if choice in menu:
            return choice
        else:
            error = True
        
    
def display_contacts():
    print("______\ncontact list\n______")
    contacts = r_file_contact()
    if not contacts :
        print("No contacts found! Add a contact first")
    else:
        for index, contact in enumerate(contacts,1):
            print(f"{index}. {contact}")
    sleep(5)
    
def search_contacts():
    print("______\nsearch contact\n______")
    query = get_search()
    contacts = r_file_contact()
    found = False
    for contact in contacts:
        if query in contact.lower():
            print(f"found: {contact}")
            found = True
    if not found:
        print("No contacts found matching your search")
    sleep(3)
    
    
def add_new_contact():
    print("______\nadd new contact\n______")
    first_name, last_name, phone, email = get_contact()
    if save_contact(first_name, last_name, phone, email):
        print("Contact saved successfully")
    else:
        print("Error saving contact")
    sleep(3)
    
    
def show_login_menu():
    login_menu={
        "1": "Login with existing user",
        "2": "Register new user"
    }
    display_menu(login_menu, "login menu")
    choice = get_menu_choice(login_menu)
    if choice == "1":
        return login_user()
    else:
        return register_new_user()


def show_menu_main():
    main_menu = {
        "1" : "add contact",
        "2" : "Contacts list",
        "3" : "Search",
        "4" : "Exit"
    }
    display_menu(main_menu, "menu:")
    return get_menu_choice(main_menu)

def call_option(choice):
    if choice == "1":
        add_new_contact()
    elif choice == "2":
        display_contacts()
    elif choice == "3":
        search_contacts()
    else:
        return False
    return True

def main():
    while True:
        if show_login_menu():
            break
        print("please try again..")
        sleep(3)
        
    while True:
        choice = show_menu_main()
        if choice == "4":
            print("bye-")
            break
        call_option(choice)

if __name__ == "__main__":
    main()