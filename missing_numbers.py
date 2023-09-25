"""
Write a function called missing_numbers that takes a list of 
sequence of numbers and finds the missing numbers in the sequence.
"""


def missing_numbers(nums: list) -> list:
    l = sorted(nums)
    l2 = []
    for i in range(l[0], l[-1] + 1):
        if i not in l:
            l2.append(i)

    return l2


list = [
    1,
    2,
    3,
    5,
    6,
    7,
    9,
    11,
    12,
    23,
    14,
    15,
    17,
    18,
    19,
    20,
    21,
    22,
    24,
    25,
    26,
    27,
    28,
    31,
]

print(missing_numbers(list))
