"""
Write a function called capitalize. This function takes a string 
as an argument and capitalizes the first letter of each word.
"""


def capitalize(string: str) -> str:
    mod = []
    for i in string.split():
        mod2 = []
        for enum, j in enumerate(i):
            if enum == 0:
                mod2.append(j.upper())
            else:
                mod2.append(j)
        mod.append("".join(mod2))
    return " ".join(mod)


string = "i like learning"
print(capitalize(string))
