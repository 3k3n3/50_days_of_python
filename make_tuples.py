"""
Write a function called make_tuples that takes two lists, 
equal lists, and combines them into a list of tuples. 
"""


def make_tuples(l1: list, l2: list) -> list:
    try:
        new = []
        for i in range(len(l1)):
            new.append((l1[i], l2[i]))
        return new

    except IndexError:
        return "Lists not equal!"


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print(make_tuples(a, b))
