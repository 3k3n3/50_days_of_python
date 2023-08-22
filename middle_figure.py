"""
Write a function called middle_figure that takes two parameters a, and b.
The two parameters are strings. The function joins the two strings and finds
the middle element. If the combined string has a middle element, the function
should return the element, otherwise, return ‘no middle figure’.
"""


def middle_figure(a: str, b: str) -> str:
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    c = f"{a}{b}"
    if len(c) % 2 == 0:
        return "no middle figure"
    else:
        return c[int(len(c) / 2 - 0.5)]


a = "make love"
b = "not wars"
print(middle_figure(a, b))
