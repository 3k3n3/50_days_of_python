"""
Write a function called find_index that takes two arguments; 
a list of integers, and an integer. The function should return the 
indexes of the integer in the list. If the integer is not in the list, 
the function should convert all the numbers in the list into the 
given integer. 
"""


def find_index(nums: list, num: int) -> list:
    x = [enum for enum, i in enumerate(nums) if i == num]
    return x if len(x) > 0 else [num for x in nums]


nums = [1, 2, 4, 6, 7, 7]
num = 7
print(find_index(nums, num))

nums = [1, 2, 4, 6, 7, 7]
num = 9
print(find_index(nums, num))
