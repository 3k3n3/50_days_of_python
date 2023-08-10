"""`
Write a function called convert_add that takes a list of strings 
as an argument and converts it to integers and sums the list.
"""


def convert_add(l: list) -> int:
    return sum([int(i) for i in l])


l = ["1", "3", "5"]
print(convert_add(l))
