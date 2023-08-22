"""
Write a function called largest_number that takes a list of integers and
re-arrange the individual digits to create the largest number possible.
"""


def largest_number(nums: list) -> str:
    return (
        f'{int("".join(sorted(list("".join([str(i) for i in nums])), reverse=True))):,}'
    )


list1 = [3, 67, 87, 9, 2]
print(largest_number(list1))
