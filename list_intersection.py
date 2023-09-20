"""
Write a function called inter_section that takes two lists and 
finds the intersection (the elements that are present in both 
lists). The function should return a tuple of intersections. Use 
list comprehension in your solution.
"""


def inter_section0(arr1: list, arr2: list) -> tuple:
    """Using set methods."""
    return tuple(sorted(set(arr1).intersection(arr2)))


def inter_section1(arr1: list, arr2: list) -> tuple:
    """Using list comprehension."""
    return tuple([x for x in arr1 if x in arr2])


list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]

print(inter_section0(list1, list2))
print(inter_section1(list1, list2))
