"""
Write a function called flat_list that takes one argument, a 
nested list. The function converts the nested list into a one-dimension list.
"""


def flat_list(nested_list: list) -> list:
    # if all nested list contains just one item
    # return nested_list[0]
    one_dim_list = []
    for i in nested_list:
        one_dim_list += i
    return one_dim_list


example1 = [[2, 4, 5, 6]]
example2 = [[2, 4, 5, 6], [9, 9], [0]]

print(flat_list(example1))
print(flat_list(example2))
