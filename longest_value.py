"""
Write a function called longest_value that takes a dictionary 
as an argument and returns the first longest value of the dictionary.
"""


def longest_value(d: dict) -> str:
    long_val = ""
    for k,v in d.items():
        if len(v) > len(long_val):
            long_val = v
    return long_val


fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))