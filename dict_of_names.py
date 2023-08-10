"""
You are given a list of names, and you are asked to write a code that returns
all the names that start with ‘S’. Your code should return a dictionary of
all the names that start with S and how many times they appear in the dictionary.
"""


def dict_of_names(names: list) -> dict:
    s_names = set([n for n in names if n.startswith("S")])
    return {k: names.count(k) for k in s_names}


names = [
    "Joseph",
    "Nathan",
    "Sasha",
    "Kelly",
    "Muhammad",
    "Jabulani",
    "Sera",
    "Patel",
    "Sera",
]

print(dict_of_names(names))
