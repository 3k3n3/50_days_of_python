"""
Write a function called sum_list with one parameter that takes a nested list
of integers as an argument and returns the sum of the integers.
"""


def sum_list(int_arr: list) -> int:
    one_dim_list = []
    for i in int_arr:
        one_dim_list += i
    return sum(one_dim_list)


arr = [[2, 4, 5, 6], [2, 3, 5, 6]]

print(sum_list(arr))
