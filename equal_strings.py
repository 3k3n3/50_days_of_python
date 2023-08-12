"""
Write a function called equal_strings. The function takes two 
strings as arguments and compares them. If the strings are equal 
(if they have the same characters and have equal length), it 
should return True, if they are not, it should return False.
"""


def equal_strings(str1: str, str2: str) -> bool:
    return sorted([i for i in str1]) == sorted([i for i in str2])


str1 = "love"
str2 = "evol"
print(equal_strings(str1, str2))
