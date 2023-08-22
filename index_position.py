"""
Write a function called index_position. This function takes a string as a
parameter and returns the positions or indexes of all lower letters in the string.
"""


def index_position(word: str) -> list:
    return [enum for enum, i in enumerate(word) if i.islower()]


word = "LovE"
print(index_position(word))
