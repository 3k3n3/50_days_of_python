"""
You are given a list of names above. This list is made up of names 
of lowercase and uppercase letters. Your task is to write a code 
that will return a tuple of all the names in the list that have only
lowercase letters. Your tuple should have names sorted 
alphabetically in descending order. 
"""


def lowercase_names(names: list) -> tuple:
    tup = []
    for i in names:
        if i[0].islower():
            tup.append(i)
    tup.sort(reverse=True)
    return tuple(tup)


names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
print(lowercase_names(names))
