"""
Create three functions. The first called add_hash takes a string and 
adds a hash # between the words
The second function called add_underscore removes the hash (#) and
replaces it with an underscore "_" 
The third function called remove_underscore, removes the underscore and
replaces it with nothing.
"""


def add_hash(string: str) -> str:
    """Takes a string and adds a hash # between the words."""
    return "#".join(string.split())


def add_underscore(string: str) -> str:
    """Removes the hash (#) and replaces it with an underscore '_'."""
    return string.replace("#", "_")


def remove_underscore(string: str) -> str:
    """Removes the underscore and replaces it with nothing."""
    return string.replace("_", "")


print(remove_underscore(add_underscore(add_hash("Python is fun"))))
