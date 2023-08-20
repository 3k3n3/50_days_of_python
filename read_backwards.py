"""
Write a function called read_backwards that takes a string as 
an argument and reverses it.
"""


def read_backwards(str1: str) -> str:
    return " ".join(str1.split()[::-1])


str1 = "the love is real"
print(read_backwards(str1=str1))
