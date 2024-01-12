import random
import string


def generate_password(min_length, numbers=True, special=True):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special:
        characters += special_char

    password = ""
    meets_req = False
    has_numbers = False
    has_special = False

    while not meets_req or len(password) <= min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_numbers = True
        if new_char in special_char:
            has_special = True

        meets_req = True
        if numbers:
            meets_req = has_numbers
        if special:
            meets_req = meets_req and has_special

    print(password)


pwd_len = int(input("Enter the lenght of the Password: "))
pwd_num = input("Do you need Numbers in your Passwords(y/n) ?").lower() == "y"
pwd_special = input("Do you need Special Characters in your Password(y/n) ?").lower() == "y"

generate_password(pwd_len, pwd_num, pwd_special)
