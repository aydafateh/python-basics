phone_number = input("Enter your phone number: ")
email_user = input("Enter your email :")
print(phone_number.isdecimal() & phone_number.startswith("09"))
print(email_user.endswith("@gmail.com"))