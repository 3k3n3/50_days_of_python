"""
Create a function called all_the_same that takes one 
argument, a string, a list, or a tuple and checks if all the 
elements are the same. If the elements are the same, the function 
should return True. If not, it should return False.
"""


def all_the_same(arg) -> bool:
    if type(arg) == str:
        arg = arg.split()

    control = arg[0]
    for a in arg:
        if a != control:
            return False
    return True


arg1 = "Mary Mary Mary"
arg2 = ("Mary", "Mary", "Mary")
arg3 = ["Mary", "Mary", "Mary"]
print(all_the_same(arg=arg1))
print(all_the_same(arg=arg2))
print(all_the_same(arg=arg3))
