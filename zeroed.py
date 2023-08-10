"""
Write a function called zeroed code that takes a list of numbers as an argument.
The code should zero (0) the first and the last number in the list.
"""


def zeroed(l: list) -> list:
    new_list = []
    for enum, i in enumerate(l):
        if enum == 0 or enum == len(l) - 1:
            new_list.append(0)
        else:
            new_list.append(i)
    return new_list


numbers = [2, 5, 7, 8, 9]

print(zeroed(numbers))
