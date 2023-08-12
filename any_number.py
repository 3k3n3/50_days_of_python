"""
Write a function called any_number that can receive any 
number of arguments (integers and floats) and return the 
average of those integers.
"""


def any_number(*args) -> float:
    return sum(args) / len(args)


print(any_number(12, 90, 12, 34))
print(any_number(12, 90))
