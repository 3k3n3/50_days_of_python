"""
Write a function called string_range that takes a single number and returns
a string of its range. The string characters should be separated by dots(.)
"""


def string_range(num: int) -> str:
    return ".".join([str(i) for i in range(num)])


print(string_range(6))
