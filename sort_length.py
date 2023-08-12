"""
Write a function called sort_length that takes a list of strings
as an argument, and sorts the strings in ascending order 
according to their length.
"""


def sort_length(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


names = ["Peter", "Jon", "Andrew", "Mo"]
print(sort_length(names))
