"""
You work for a local school in your area. The school has a list of 
names of students saved in a list. The school has asked you to 
write a program that takes a list of names and sorts them
alphabetically. The names should be sorted by last names.
Your code should not just sort them alphabetically, but it should 
also switch the names (the last name must be the first).
"""


def sorted_names(names: list) -> list:
    new = []
    for i in names:
        i = i.split()
        i[0], i[1] = i[1], i[0]
        new.append(" ".join(i))

    return sorted(new)


names = ["Beyonce Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise"]
print(sorted_names(names))
