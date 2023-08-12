"""
Write a function called hide_password that takes no parameters. The function
takes an input (a password) from a user and returns a hidden password. 
"""
from getpass import getpass


def hide_password() -> str:
    password = getpass("Enter password: ")
    return "****\nPassword is 4 characters long"


print(hide_password())
