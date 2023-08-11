"""
Create a function called biggest_odd that takes a string of 
numbers and returns the biggest odd number in the list.
"""


def biggest_odd(nums: str) -> int:
    return max([int(x) for x in nums])


print(biggest_odd("23569"))
