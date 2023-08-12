"""
Write a function called age_in_minutes that tells a user how 
old they are in minutes. Your code should ask the user to 
enter their year of birth, and it should return their age in 
minutes (by subtracting their year of birth to the current year). 
Here are things to look out for:
a. The user can only input a 4-digit year of birth. For 
example, 1930 is a valid year. However, entering any 
number longer or less than 4 digits long should render 
input invalid. Notify the user to input a four digits 
number.
b. If a user enters a year before 1900, your code should 
tell the user that input is invalid. If the user enters the 
year after the current year, the code should tell the user, 
to input a valid year.
The code should run until the user inputs a valid year.
"""
from datetime import datetime


def age_in_minutes() -> str:
    this_year = datetime.now().year
    your_year = input("Enter your year of birth: ")
    if len(your_year) != 4:
        print("Enter a 4 digit number.")
        age_in_minutes()
    else:
        try:
            your_year = int(your_year)
            if your_year < 1900 or your_year > this_year:
                print("Enter a valid year: ")
                age_in_minutes()
            else:
                return f"You are {((this_year - your_year) * 525600):,} minutes old"
        except Exception:
            print("Enter a valid year: ")
            age_in_minutes()


print(age_in_minutes())
