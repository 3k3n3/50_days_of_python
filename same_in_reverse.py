"""
Write a function called same_in_reverse that takes a string 
and checks if the string reads the same in reverse. If it is the 
same, the code should return True if not, it should return False. 
"""


def same_in_reverse(word: str) -> bool:
    return word == "".join([i for i in reversed(word)])


print(same_in_reverse("dad"))
print(same_in_reverse("madam"))
print(same_in_reverse("road"))
