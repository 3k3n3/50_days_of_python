"""
Write a function called odd_even that has one parameter and
takes a list of numbers as an argument. The function returns the 
difference between the largest even number in the list and the 
smallest odd number in the list.
"""


def odd_even(nums: list) -> int:
    return max(nums) - min(nums)


nums = [1, 2, 4, 6]
print(odd_even(nums))
