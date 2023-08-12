"""
Write a function called user_name, that creates a username 
for the user. The function should ask a user to input their name. 
The function should then reverse the name and attach a 
randomly issued number between 0 – 9 at the end of the name. 
The function should return the username.
"""
import random


def user_name() -> str:
    while True:
        try:
            name = input("Enter your name: ")
            if any(x.isnumeric() for x in name):
                raise ValueError("That's not a name, try again!")
        except ValueError:
            print("That's not a name, try again!")
        else:
            # reverse name, select random number from range 0 - 9
            return f"{''.join([x for x in reversed(name)])}{random.choice(range(10))}"


print(user_name())
