"""
Write a function called count that takes one argument a string, 
and returns a dictionary of how many times each element 
appears in the string.
"""


def count(string: str):
    return {k: string.count(k) for k in string}


string = "hello"

print(count(string=string))
