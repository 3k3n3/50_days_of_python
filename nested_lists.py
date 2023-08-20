"""
Write a function called nested_lists that takes any number of 
lists and creates a 2-dimensional nested list of lists.
"""


def nested_lists(lists: tuple) -> list:
    return list(lists)


lists = [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]
print(nested_lists(lists))
