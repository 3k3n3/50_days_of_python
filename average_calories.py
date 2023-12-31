"""
Create a function called average_calories that calculates the 
average calories intake of a user. The function should ask the user 
to input their calories intake for any number of days and once they 
hit ‘done’ it should calculate and return the average intake.
"""


def average_calories() -> float:
    while True:
        try:
            calories = int(input("Enter calories intake: "))
            days = int(input("Enter number of days: "))
            return calories / days
        except ValueError:
            print("Invalid input")


print(average_calories())
