"""
Write a function called repeated_name that finds the most repeated name in a list.
"""


def repeated_name(names: list) -> str:
    n = 0
    nm = ""
    for name in names:
        # save count of name with highes count as n
        # change nm to most counted name
        if names.count(name) > n:
            n = names.count(name)
            nm = name
    return nm


name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(name))
