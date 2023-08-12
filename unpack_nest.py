"""
Write a code that generates a list of the following numbers from 
the nested list above – 34, 67, 78. Your output should be another list.
"""


def unpack_nest(nest: list) -> list:
    new = []
    for i in nest:
        new.append(i[-3])
        new.append(i[-1])
    return list(set(new))


nested_list = [[12, 34, 56, 67], [34, 68, 78]]
print(unpack_nest(nested_list))
