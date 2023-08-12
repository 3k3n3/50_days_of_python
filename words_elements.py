"""
Write two functions. The first function is called count_words which takes
a string of words and counts how many words are in the string.

The second function called count_elements takes a string of words and counts
how many elements are in the string. Do not count the whitespaces.

The first function will return the number of words in a string and the second
one will return the number of elements (less whitespace).
"""


def count_words(string: str) -> int:
    # split into list and return length of list
    return len(string.split())


def count_elements(strind: str) -> int:
    # join list items from above and return length of new string
    return len("".join(string.split()))


string = "I love learning"
print(count_words(string))
print(count_elements(string))
