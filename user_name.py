"""
Write a function called user_name that generates a username from the 
user’s email. The code should ask the user to input an email and the code
should return everything before the @ sign as their user name
"""
import re

regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


def user_name() -> str:
    email = input("Enter your email: ")
    if re.fullmatch(regex, email):
        return email[: email.index("@")]
    else:
        print("Invalid Email")
        user_name()


print(user_name())
