"""
Create a function called generate_password that generates any 
length of password for the user. The password should have a 
random mix of upper letters, lower letters, numbers, and 
punctuation symbols. The function should ask the user how 
strong they want the password to be. The user should pick from - 
weak, strong, and very strong. If the user picks weak, the 
function should generate a 5-character long password. If the user 
picks strong, generate an 8-character password and if they pick 
very strong, generate a 12-character password.
"""

import string
import random


def generate_password() -> str:
    chars = string.ascii_letters + string.punctuation + string.digits

    print("Select Password strength:")

    strength = input('"w" for weak\n"s" for strong\n"v" for very strong\n: ').lower()

    if strength == "w":
        password = random.choices(chars, k=5)
        return "".join(password)

    elif strength == "s":
        password = random.choices(chars, k=8)
        return "".join(password)

    elif strength == "v":
        password = random.choices(chars, k=12)
        return "".join(password)

    else:
        print("Invalid Input!")
        return generate_password()


print(generate_password())
