"""
Write a function called swap_values. This function takes a list 
of numbers and swaps the first element with the last element.
"""


def swap_values(nums: list) -> list:
    x = nums[-1]
    nums[-1] = nums[0]
    nums[0] = x

    return nums


nums = [2, 4, 67, 7]
print(swap_values(nums))
