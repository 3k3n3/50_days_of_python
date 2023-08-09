"""
Write a function called check_duplicates that takes a list of strings
as an argument. The function should check if the list has any duplicates.
If there are duplicates, the function should return the duplicates.
If there are no duplicates, the function should return "No duplicates".
"""


def check_duplicates(l: list) -> str:
    for i in l:
        if l.count(i) > 1:
            return i
    else:
        return "No duplicates"


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
print(check_duplicates(fruits))
print(check_duplicates(names))