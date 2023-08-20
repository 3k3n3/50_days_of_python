"""
Write a function called string_length that takes a string of words
(words and spaces) as argument. This function should return the length
of all the words in the string. Return the results in a form of a dictionary.
"""


def string_length(string: str) -> dict:
    return {k: len(k) for k in string.split()}


s = "Hi my name is Richard"
print(string_length(s))
