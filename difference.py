"""
Write a function called difference that takes two lists as arguments.
This function should return all the elements that are in list
a but not in list b and all the elements in list b not in list a.
"""


def difference_1(a: list, b: list) -> list:
    # Use list comprehension in your function.
    return [i for i in a if i not in b] + [i for i in b if i not in a]


def difference_2(a: list, b: list) -> list:
    return list(set(a).symmetric_difference(set(b)))


list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]

print(difference_1(list1, list2))
print(difference_2(list1, list2))
