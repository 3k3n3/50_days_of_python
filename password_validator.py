"""
Write a function called password_validator. The function 
asks the user to enter a password. A valid password should have 
at least one upper letter, one lower letter, and one 
number. It should not be less than 8 characters long. When 
the user enters a password, the function should check if the 
password is valid. If the password is valid, the function should 
return the valid password. If the password is not valid, the 
function should tell the users the errors in the password and 
prompt the user to enter another password. The code should 
only stop once the user enters a valid password. (use while loop).
"""


def password_validator() -> str:
    while True:
        password = input("Enter password: ")
        if len(password) < 8:
            print("Password too short, minimum is 8 chars.")
        if not any(i.isupper() for i in password):
            print("Password must contain at least one uppercase char.")
        if not any(i.islower() for i in password):
            print("Password must contain at least one lowercase char.")
        if not any(i.isnumeric() for i in password):
            print("Password must contain at least one number.")

        else:
            return password


print(password_validator())
