"""
Write a function called create_user. This function asks the 
user to enter their name, age, and password. The function 
saves this information in a dictionary. 
Once the information is saved. The function should print to the 
user that - "User saved. Please login"
The function should then ask the user to re-enter their name 
and password. If the name and password match with what is 
saved in the dictionary, the function should return "Logged in 
successfully". If the name and password do not match with 
what is saved in the dictionary, the function should print
('Wrong password or user name. Please try again'. The function
should keep running until the user enters correct logging details
"""
import pwinput


def create_user():
    global name, age, password
    try:
        name = input("Enter your name: ")
        if name == "":
            print("---Name cannot be blank!")
            raise ValueError
        age = int(input("Enter your age: "))
        password = pwinput.pwinput(prompt="Enter your password: ")
        if password == "":
            print("---Password cannot be empty!")
            raise ValueError

    except ValueError:
        print("Enter valid details!")
        create_user()

    else:
        user = {"name": name, "age": age, "password": password}
        print("User saved. Please login")

        while True:
            print("LOGIN")
            user_name = input("Username: ")
            user_password = pwinput.pwinput(prompt="Password: ")

            if user["name"] == user_name and user["password"] == user_password:
                return "Logged in successfully!"
            else:
                print("Wrong password or username. Please Try again")

    return "Logged in successfully!"


# create_user()
print(create_user())
