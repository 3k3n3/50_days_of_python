"""
Write a function called add_reverse. This function takes two
lists as argument and adds each corresponding number, and 
reverses the outcome.
"""


def add_reverse(arr1: list, arr2: list) -> list:
    if len(arr1) != len(arr2):
        return "The lists are not of equal lengths."

    else:
        new = []
        for i in range(len(arr1)):
            new.append(arr1[i] + arr2[i])
            # reverses new list after each addition
            # new.reverse()
    new.reverse()
    return new


list1 = [10, 12, 34]
list2 = [12, 56, 78]

print(add_reverse(list1, list2))
