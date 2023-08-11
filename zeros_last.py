"""
Write a function called zeros_last. This function takes a list as argument.
If a list has zeros (0), it will move them to the front of the list and
maintain the order of the other numbers in the list. If there are no Zeros
in the list, the function should return the original list sorted in ascending order.
"""


def zeros_last(arr: list) -> list:
    if 0 in arr:
        return [i for i in arr if i != 0] + [i for i in arr if i == 0]
    else:
        return sorted(arr)


arr1 = [1, 4, 6, 0, 7, 0, 9]
arr2 = [2, 1, 4, 7, 6]

print(zeros_last(arr=arr1))
print(zeros_last(arr=arr2))
